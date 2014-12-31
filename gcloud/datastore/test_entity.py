# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest2

_MARKER = object()
_DATASET_ID = 'DATASET'
_KIND = 'KIND'
_ID = 1234


class TestEntity(unittest2.TestCase):

    def _getTargetClass(self):
        from gcloud.datastore import _implicit_environ
        from gcloud.datastore.entity import Entity

        _implicit_environ.DATASET = None
        return Entity

    def _makeOne(self, dataset=_MARKER, kind=_KIND, exclude_from_indexes=()):
        from gcloud.datastore.dataset import Dataset

        klass = self._getTargetClass()
        if dataset is _MARKER:
            dataset = Dataset(_DATASET_ID)
        return klass(dataset, kind, exclude_from_indexes)

    def test_ctor_defaults(self):
        klass = self._getTargetClass()
        entity = klass()
        self.assertEqual(entity.key(), None)
        self.assertEqual(entity.dataset(), None)
        self.assertEqual(entity.kind(), None)
        self.assertEqual(sorted(entity.exclude_from_indexes()), [])

    def test_ctor_explicit(self):
        from gcloud.datastore.dataset import Dataset

        dataset = Dataset(_DATASET_ID)
        _EXCLUDE_FROM_INDEXES = ['foo', 'bar']
        entity = self._makeOne(dataset, _KIND, _EXCLUDE_FROM_INDEXES)
        self.assertTrue(entity.dataset() is dataset)
        self.assertEqual(sorted(entity.exclude_from_indexes()),
                         sorted(_EXCLUDE_FROM_INDEXES))

    def test_key_getter(self):
        from gcloud.datastore.key import Key

        entity = self._makeOne()
        key = entity.key()
        self.assertIsInstance(key, Key)
        self.assertEqual(key.dataset_id, None)
        self.assertEqual(key.kind, _KIND)

    def test_key_setter(self):
        entity = self._makeOne()
        key = object()
        entity.key(key)
        self.assertTrue(entity.key() is key)

    def test_from_key_wo_dataset(self):
        from gcloud.datastore.key import Key

        klass = self._getTargetClass()
        key = Key(_KIND, _ID, dataset_id='DATASET')
        entity = klass.from_key(key)
        self.assertTrue(entity.dataset() is None)
        self.assertEqual(entity.kind(), _KIND)
        key = entity.key()
        self.assertEqual(key.kind, _KIND)
        self.assertEqual(key.id, _ID)

    def test_from_key_w_dataset(self):
        from gcloud.datastore.dataset import Dataset
        from gcloud.datastore.key import Key

        klass = self._getTargetClass()
        dataset = Dataset(_DATASET_ID)
        key = Key(_KIND, _ID, dataset_id=_DATASET_ID)
        entity = klass.from_key(key, dataset)
        self.assertTrue(entity.dataset() is dataset)
        self.assertEqual(entity.kind(), _KIND)
        key = entity.key()
        self.assertEqual(key.kind, _KIND)
        self.assertEqual(key.id, _ID)

    def test__must_key_no_key(self):
        from gcloud.datastore.entity import NoKey

        entity = self._makeOne(None, None)
        self.assertRaises(NoKey, getattr, entity, '_must_key')

    def test__must_dataset_no_dataset(self):
        from gcloud.datastore.entity import NoDataset

        entity = self._makeOne(None, None)
        self.assertRaises(NoDataset, getattr, entity, '_must_dataset')

    def test_reload_no_key(self):
        from gcloud.datastore.entity import NoKey

        entity = self._makeOne(None, None)
        entity['foo'] = 'Foo'
        self.assertRaises(NoKey, entity.reload)

    def test_reload_miss(self):
        dataset = _Dataset()
        key = _Key()
        entity = self._makeOne(dataset)
        entity.key(key)
        entity['foo'] = 'Foo'
        # Does not raise, does not update on miss.
        self.assertTrue(entity.reload() is entity)
        self.assertEqual(entity['foo'], 'Foo')

    def test_reload_hit(self):
        dataset = _Dataset()
        dataset['KEY'] = {'foo': 'Bar'}
        key = _Key()
        entity = self._makeOne(dataset)
        entity.key(key)
        entity['foo'] = 'Foo'
        self.assertTrue(entity.reload() is entity)
        self.assertEqual(entity['foo'], 'Bar')

    def test_save_no_key(self):
        from gcloud.datastore.entity import NoKey

        entity = self._makeOne(None, None)
        entity['foo'] = 'Foo'
        self.assertRaises(NoKey, entity.save)

    def test_save_wo_transaction_wo_auto_id_wo_returned_key(self):
        connection = _Connection()
        dataset = _Dataset(connection)
        key = _Key()
        entity = self._makeOne(dataset)
        entity.key(key)
        entity['foo'] = 'Foo'
        self.assertTrue(entity.save() is entity)
        self.assertEqual(entity['foo'], 'Foo')
        self.assertEqual(connection._saved,
                         (_DATASET_ID, 'KEY', {'foo': 'Foo'}, ()))
        self.assertEqual(key._path, None)

    def test_save_w_transaction_wo_partial_key(self):
        connection = _Connection()
        transaction = connection._transaction = _Transaction()
        dataset = _Dataset(connection)
        key = _Key()
        entity = self._makeOne(dataset)
        entity.key(key)
        entity['foo'] = 'Foo'
        self.assertTrue(entity.save() is entity)
        self.assertEqual(entity['foo'], 'Foo')
        self.assertEqual(connection._saved,
                         (_DATASET_ID, 'KEY', {'foo': 'Foo'}, ()))
        self.assertEqual(transaction._added, ())
        self.assertEqual(key._path, None)

    def test_save_w_transaction_w_partial_key(self):
        connection = _Connection()
        transaction = connection._transaction = _Transaction()
        dataset = _Dataset(connection)
        key = _Key()
        key._partial = True
        entity = self._makeOne(dataset)
        entity.key(key)
        entity['foo'] = 'Foo'
        self.assertTrue(entity.save() is entity)
        self.assertEqual(entity['foo'], 'Foo')
        self.assertEqual(connection._saved,
                         (_DATASET_ID, 'KEY', {'foo': 'Foo'}, ()))
        self.assertEqual(transaction._added, (entity,))
        self.assertEqual(key._path, None)

    def test_save_w_returned_key_exclude_from_indexes(self):
        from gcloud.datastore import datastore_v1_pb2 as datastore_pb
        from gcloud.datastore.key import Key

        key_pb = datastore_pb.Key()
        key_pb.partition_id.dataset_id = _DATASET_ID
        key_pb.path_element.add(kind=_KIND, id=_ID)
        connection = _Connection()
        connection._save_result = key_pb
        dataset = _Dataset(connection)
        key = Key('KIND', dataset_id='DATASET')
        entity = self._makeOne(dataset, exclude_from_indexes=['foo'])
        entity.key(key)
        entity['foo'] = 'Foo'
        self.assertTrue(entity.save() is entity)
        self.assertEqual(entity['foo'], 'Foo')
        self.assertEqual(connection._saved[0], _DATASET_ID)
        self.assertEqual(connection._saved[1], key.to_protobuf())
        self.assertEqual(connection._saved[2], {'foo': 'Foo'})
        self.assertEqual(connection._saved[3], ('foo',))
        self.assertEqual(len(connection._saved), 4)

        self.assertEqual(entity.key()._path, [{'kind': _KIND, 'id': _ID}])

    def test_delete_no_key(self):
        from gcloud.datastore.entity import NoKey

        entity = self._makeOne(None, None)
        entity['foo'] = 'Foo'
        self.assertRaises(NoKey, entity.delete)

    def test_delete(self):
        connection = _Connection()
        dataset = _Dataset(connection)
        key = _Key()
        entity = self._makeOne(dataset)
        entity.key(key)
        entity['foo'] = 'Foo'
        self.assertTrue(entity.delete() is None)
        self.assertEqual(connection._deleted, (_DATASET_ID, ['KEY']))

    def test___repr___no_key_empty(self):
        entity = self._makeOne(None, None)
        self.assertEqual(repr(entity), '<Entity {}>')

    def test___repr___w_key_non_empty(self):
        connection = _Connection()
        dataset = _Dataset(connection)
        key = _Key()
        key._path = '/bar/baz'
        entity = self._makeOne(dataset)
        entity.key(key)
        entity['foo'] = 'Foo'
        self.assertEqual(repr(entity), "<Entity/bar/baz {'foo': 'Foo'}>")


class _Key(object):
    _MARKER = object()
    _key = 'KEY'
    _partial = False
    _path = None
    _id = None

    def to_protobuf(self):
        return self._key

    @property
    def is_partial(self):
        return self._partial

    @property
    def path(self):
        return self._path


class _Dataset(dict):

    def __init__(self, connection=None):
        super(_Dataset, self).__init__()
        self._connection = connection

    def __bool__(self):
        # Make sure the objects are Truth-y since an empty
        # dict with _connection set will still be False-y.
        return True

    __nonzero__ = __bool__

    def id(self):
        return _DATASET_ID

    def connection(self):
        return self._connection

    def get_entity(self, key):
        return self.get(key)

    def get_entities(self, keys):
        return [self.get(key) for key in keys]

    def allocate_ids(self, incomplete_key, num_ids):
        def clone_with_new_id(key, new_id):
            clone = key._clone()
            clone._path[-1]['id'] = new_id
            return clone
        return [clone_with_new_id(incomplete_key, i + 1)
                for i in range(num_ids)]


class _Connection(object):
    _transaction = _saved = _deleted = None
    _save_result = True

    def transaction(self):
        return self._transaction

    def save_entity(self, dataset_id, key_pb, properties,
                    exclude_from_indexes=()):
        self._saved = (dataset_id, key_pb, properties,
                       tuple(exclude_from_indexes))
        return self._save_result

    def delete_entities(self, dataset_id, key_pbs):
        self._deleted = (dataset_id, key_pbs)


class _Transaction(object):
    _added = ()

    def __nonzero__(self):
        return True
    __bool__ = __nonzero__

    def add_auto_id_entity(self, entity):
        self._added += (entity,)
