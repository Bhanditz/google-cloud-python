# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/iam/credentials/v1/common.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/iam/credentials/v1/common.proto",
    package="google.iam.credentials.v1",
    syntax="proto3",
    serialized_pb=_b(
        '\n&google/iam/credentials/v1/common.proto\x12\x19google.iam.credentials.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"y\n\x1aGenerateAccessTokenRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdelegates\x18\x02 \x03(\t\x12\r\n\x05scope\x18\x04 \x03(\t\x12+\n\x08lifetime\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration"d\n\x1bGenerateAccessTokenResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12/\n\x0b\x65xpire_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"C\n\x0fSignBlobRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdelegates\x18\x03 \x03(\t\x12\x0f\n\x07payload\x18\x05 \x01(\x0c"7\n\x10SignBlobResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x13\n\x0bsigned_blob\x18\x04 \x01(\x0c"B\n\x0eSignJwtRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdelegates\x18\x03 \x03(\t\x12\x0f\n\x07payload\x18\x05 \x01(\t"5\n\x0fSignJwtResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\nsigned_jwt\x18\x02 \x01(\t"b\n\x16GenerateIdTokenRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdelegates\x18\x02 \x03(\t\x12\x10\n\x08\x61udience\x18\x03 \x01(\t\x12\x15\n\rinclude_email\x18\x04 \x01(\x08"(\n\x17GenerateIdTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t"U\n)GenerateIdentityBindingAccessTokenRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x03(\t\x12\x0b\n\x03jwt\x18\x03 \x01(\t"s\n*GenerateIdentityBindingAccessTokenResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12/\n\x0b\x65xpire_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x8b\x01\n#com.google.cloud.iam.credentials.v1B\x19IAMCredentialsCommonProtoP\x01ZDgoogle.golang.org/genproto/googleapis/iam/credentials/v1;credentials\xf8\x01\x01\x62\x06proto3'
    ),
    dependencies=[
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_GENERATEACCESSTOKENREQUEST = _descriptor.Descriptor(
    name="GenerateAccessTokenRequest",
    full_name="google.iam.credentials.v1.GenerateAccessTokenRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.iam.credentials.v1.GenerateAccessTokenRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="delegates",
            full_name="google.iam.credentials.v1.GenerateAccessTokenRequest.delegates",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="scope",
            full_name="google.iam.credentials.v1.GenerateAccessTokenRequest.scope",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="lifetime",
            full_name="google.iam.credentials.v1.GenerateAccessTokenRequest.lifetime",
            index=3,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=134,
    serialized_end=255,
)


_GENERATEACCESSTOKENRESPONSE = _descriptor.Descriptor(
    name="GenerateAccessTokenResponse",
    full_name="google.iam.credentials.v1.GenerateAccessTokenResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="access_token",
            full_name="google.iam.credentials.v1.GenerateAccessTokenResponse.access_token",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="expire_time",
            full_name="google.iam.credentials.v1.GenerateAccessTokenResponse.expire_time",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=257,
    serialized_end=357,
)


_SIGNBLOBREQUEST = _descriptor.Descriptor(
    name="SignBlobRequest",
    full_name="google.iam.credentials.v1.SignBlobRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.iam.credentials.v1.SignBlobRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="delegates",
            full_name="google.iam.credentials.v1.SignBlobRequest.delegates",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.iam.credentials.v1.SignBlobRequest.payload",
            index=2,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=359,
    serialized_end=426,
)


_SIGNBLOBRESPONSE = _descriptor.Descriptor(
    name="SignBlobResponse",
    full_name="google.iam.credentials.v1.SignBlobResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key_id",
            full_name="google.iam.credentials.v1.SignBlobResponse.key_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="signed_blob",
            full_name="google.iam.credentials.v1.SignBlobResponse.signed_blob",
            index=1,
            number=4,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=428,
    serialized_end=483,
)


_SIGNJWTREQUEST = _descriptor.Descriptor(
    name="SignJwtRequest",
    full_name="google.iam.credentials.v1.SignJwtRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.iam.credentials.v1.SignJwtRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="delegates",
            full_name="google.iam.credentials.v1.SignJwtRequest.delegates",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.iam.credentials.v1.SignJwtRequest.payload",
            index=2,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=485,
    serialized_end=551,
)


_SIGNJWTRESPONSE = _descriptor.Descriptor(
    name="SignJwtResponse",
    full_name="google.iam.credentials.v1.SignJwtResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key_id",
            full_name="google.iam.credentials.v1.SignJwtResponse.key_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="signed_jwt",
            full_name="google.iam.credentials.v1.SignJwtResponse.signed_jwt",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=553,
    serialized_end=606,
)


_GENERATEIDTOKENREQUEST = _descriptor.Descriptor(
    name="GenerateIdTokenRequest",
    full_name="google.iam.credentials.v1.GenerateIdTokenRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.iam.credentials.v1.GenerateIdTokenRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="delegates",
            full_name="google.iam.credentials.v1.GenerateIdTokenRequest.delegates",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="audience",
            full_name="google.iam.credentials.v1.GenerateIdTokenRequest.audience",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="include_email",
            full_name="google.iam.credentials.v1.GenerateIdTokenRequest.include_email",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=608,
    serialized_end=706,
)


_GENERATEIDTOKENRESPONSE = _descriptor.Descriptor(
    name="GenerateIdTokenResponse",
    full_name="google.iam.credentials.v1.GenerateIdTokenResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="token",
            full_name="google.iam.credentials.v1.GenerateIdTokenResponse.token",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=708,
    serialized_end=748,
)


_GENERATEIDENTITYBINDINGACCESSTOKENREQUEST = _descriptor.Descriptor(
    name="GenerateIdentityBindingAccessTokenRequest",
    full_name="google.iam.credentials.v1.GenerateIdentityBindingAccessTokenRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.iam.credentials.v1.GenerateIdentityBindingAccessTokenRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="scope",
            full_name="google.iam.credentials.v1.GenerateIdentityBindingAccessTokenRequest.scope",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="jwt",
            full_name="google.iam.credentials.v1.GenerateIdentityBindingAccessTokenRequest.jwt",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=750,
    serialized_end=835,
)


_GENERATEIDENTITYBINDINGACCESSTOKENRESPONSE = _descriptor.Descriptor(
    name="GenerateIdentityBindingAccessTokenResponse",
    full_name="google.iam.credentials.v1.GenerateIdentityBindingAccessTokenResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="access_token",
            full_name="google.iam.credentials.v1.GenerateIdentityBindingAccessTokenResponse.access_token",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="expire_time",
            full_name="google.iam.credentials.v1.GenerateIdentityBindingAccessTokenResponse.expire_time",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=837,
    serialized_end=952,
)

_GENERATEACCESSTOKENREQUEST.fields_by_name[
    "lifetime"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_GENERATEACCESSTOKENRESPONSE.fields_by_name[
    "expire_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GENERATEIDENTITYBINDINGACCESSTOKENRESPONSE.fields_by_name[
    "expire_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name[
    "GenerateAccessTokenRequest"
] = _GENERATEACCESSTOKENREQUEST
DESCRIPTOR.message_types_by_name[
    "GenerateAccessTokenResponse"
] = _GENERATEACCESSTOKENRESPONSE
DESCRIPTOR.message_types_by_name["SignBlobRequest"] = _SIGNBLOBREQUEST
DESCRIPTOR.message_types_by_name["SignBlobResponse"] = _SIGNBLOBRESPONSE
DESCRIPTOR.message_types_by_name["SignJwtRequest"] = _SIGNJWTREQUEST
DESCRIPTOR.message_types_by_name["SignJwtResponse"] = _SIGNJWTRESPONSE
DESCRIPTOR.message_types_by_name["GenerateIdTokenRequest"] = _GENERATEIDTOKENREQUEST
DESCRIPTOR.message_types_by_name["GenerateIdTokenResponse"] = _GENERATEIDTOKENRESPONSE
DESCRIPTOR.message_types_by_name[
    "GenerateIdentityBindingAccessTokenRequest"
] = _GENERATEIDENTITYBINDINGACCESSTOKENREQUEST
DESCRIPTOR.message_types_by_name[
    "GenerateIdentityBindingAccessTokenResponse"
] = _GENERATEIDENTITYBINDINGACCESSTOKENRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateAccessTokenRequest = _reflection.GeneratedProtocolMessageType(
    "GenerateAccessTokenRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GENERATEACCESSTOKENREQUEST,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      name:
          The resource name of the service account for which the
          credentials are requested, in the following format:
          ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
      delegates:
          The sequence of service accounts in a delegation chain. Each
          service account must be granted the
          ``roles/iam.serviceAccountTokenCreator`` role on its next
          service account in the chain. The last service account in the
          chain must be granted the
          ``roles/iam.serviceAccountTokenCreator`` role on the service
          account that is specified in the ``name`` field of the
          request.  The delegates must have the following format:
          ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``
      scope:
          Code to identify the scopes to be included in the OAuth 2.0
          access token. See
          https://developers.google.com/identity/protocols/googlescopes
          for more information. At least one value required.
      lifetime:
          The desired lifetime duration of the access token in seconds.
          Must be set to a value less than or equal to 3600 (1 hour). If
          a value is not specified, the token's lifetime will be set to
          a default value of one hour.
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateAccessTokenRequest)
    ),
)
_sym_db.RegisterMessage(GenerateAccessTokenRequest)

GenerateAccessTokenResponse = _reflection.GeneratedProtocolMessageType(
    "GenerateAccessTokenResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GENERATEACCESSTOKENRESPONSE,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      access_token:
          The OAuth 2.0 access token.
      expire_time:
          Token expiration time. The expiration time is always set.
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateAccessTokenResponse)
    ),
)
_sym_db.RegisterMessage(GenerateAccessTokenResponse)

SignBlobRequest = _reflection.GeneratedProtocolMessageType(
    "SignBlobRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SIGNBLOBREQUEST,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      name:
          The resource name of the service account for which the
          credentials are requested, in the following format:
          ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
      delegates:
          The sequence of service accounts in a delegation chain. Each
          service account must be granted the
          ``roles/iam.serviceAccountTokenCreator`` role on its next
          service account in the chain. The last service account in the
          chain must be granted the
          ``roles/iam.serviceAccountTokenCreator`` role on the service
          account that is specified in the ``name`` field of the
          request.  The delegates must have the following format:
          ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``
      payload:
          The bytes to sign.
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.SignBlobRequest)
    ),
)
_sym_db.RegisterMessage(SignBlobRequest)

SignBlobResponse = _reflection.GeneratedProtocolMessageType(
    "SignBlobResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SIGNBLOBRESPONSE,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      key_id:
          The ID of the key used to sign the blob.
      signed_blob:
          The signed blob.
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.SignBlobResponse)
    ),
)
_sym_db.RegisterMessage(SignBlobResponse)

SignJwtRequest = _reflection.GeneratedProtocolMessageType(
    "SignJwtRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SIGNJWTREQUEST,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      name:
          The resource name of the service account for which the
          credentials are requested, in the following format:
          ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
      delegates:
          The sequence of service accounts in a delegation chain. Each
          service account must be granted the
          ``roles/iam.serviceAccountTokenCreator`` role on its next
          service account in the chain. The last service account in the
          chain must be granted the
          ``roles/iam.serviceAccountTokenCreator`` role on the service
          account that is specified in the ``name`` field of the
          request.  The delegates must have the following format:
          ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``
      payload:
          The JWT payload to sign: a JSON object that contains a JWT
          Claims Set.
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.SignJwtRequest)
    ),
)
_sym_db.RegisterMessage(SignJwtRequest)

SignJwtResponse = _reflection.GeneratedProtocolMessageType(
    "SignJwtResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SIGNJWTRESPONSE,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      key_id:
          The ID of the key used to sign the JWT.
      signed_jwt:
          The signed JWT.
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.SignJwtResponse)
    ),
)
_sym_db.RegisterMessage(SignJwtResponse)

GenerateIdTokenRequest = _reflection.GeneratedProtocolMessageType(
    "GenerateIdTokenRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GENERATEIDTOKENREQUEST,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      name:
          The resource name of the service account for which the
          credentials are requested, in the following format:
          ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
      delegates:
          The sequence of service accounts in a delegation chain. Each
          service account must be granted the
          ``roles/iam.serviceAccountTokenCreator`` role on its next
          service account in the chain. The last service account in the
          chain must be granted the
          ``roles/iam.serviceAccountTokenCreator`` role on the service
          account that is specified in the ``name`` field of the
          request.  The delegates must have the following format:
          ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``
      audience:
          The audience for the token, such as the API or account that
          this token grants access to.
      include_email:
          Include the service account email in the token. If set to
          ``true``, the token will contain ``email`` and
          ``email_verified`` claims.
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateIdTokenRequest)
    ),
)
_sym_db.RegisterMessage(GenerateIdTokenRequest)

GenerateIdTokenResponse = _reflection.GeneratedProtocolMessageType(
    "GenerateIdTokenResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GENERATEIDTOKENRESPONSE,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      token:
          The OpenId Connect ID token.
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateIdTokenResponse)
    ),
)
_sym_db.RegisterMessage(GenerateIdTokenResponse)

GenerateIdentityBindingAccessTokenRequest = _reflection.GeneratedProtocolMessageType(
    "GenerateIdentityBindingAccessTokenRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GENERATEIDENTITYBINDINGACCESSTOKENREQUEST,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      name:
          The resource name of the service account for which the
          credentials are requested, in the following format:
          ``projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}``.
      scope:
          Code to identify the scopes to be included in the OAuth 2.0
          access token. See
          https://developers.google.com/identity/protocols/googlescopes
          for more information. At least one value required.
      jwt:
          Required. Input token. Must be in JWT format according to
          RFC7523 (https://tools.ietf.org/html/rfc7523) and must have
          'kid' field in the header. Supported signing algorithms: RS256
          (RS512, ES256, ES512 coming soon). Mandatory payload fields
          (along the lines of RFC 7523, section 3): - iss: issuer of the
          token. Must provide a discovery document at $iss/.well-
          known/openid-configuration . The document needs to be
          formatted according to section 4.2 of the OpenID Connect
          Discovery 1.0 specification. - iat: Issue time in seconds
          since epoch. Must be in the past. - exp: Expiration time in
          seconds since epoch. Must be less than 48 hours after iat. We
          recommend to create tokens that last shorter than 6 hours to
          improve security unless business reasons mandate longer
          expiration times. Shorter token lifetimes are generally more
          secure since tokens that have been exfiltrated by attackers
          can be used for a shorter time. you can configure the maximum
          lifetime of the incoming token in the configuration of the
          mapper. The resulting Google token will expire within an hour
          or at "exp", whichever is earlier. - sub: JWT subject,
          identity asserted in the JWT. - aud: Configured in the mapper
          policy. By default the service account email.  Claims from the
          incoming token can be transferred into the output token
          accoding to the mapper configuration. The outgoing claim size
          is limited. Outgoing claims size must be less than 4kB
          serialized as JSON without whitespace.  Example header: {
          "alg": "RS256", "kid":
          "92a4265e14ab04d4d228a48d10d4ca31610936f8" } Example payload:
          { "iss": "https://accounts.google.com", "iat": 1517963104,
          "exp": 1517966704, "aud":
          "https://iamcredentials.googleapis.com/", "sub":
          "113475438248934895348", "my\_claims": { "additional\_claim":
          "value" } }
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateIdentityBindingAccessTokenRequest)
    ),
)
_sym_db.RegisterMessage(GenerateIdentityBindingAccessTokenRequest)

GenerateIdentityBindingAccessTokenResponse = _reflection.GeneratedProtocolMessageType(
    "GenerateIdentityBindingAccessTokenResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GENERATEIDENTITYBINDINGACCESSTOKENRESPONSE,
        __module__="google.iam.credentials.v1.common_pb2",
        __doc__="""
Attributes:
      access_token:
          The OAuth 2.0 access token.
      expire_time:
          Token expiration time. The expiration time is always set.
  """,
        # @@protoc_insertion_point(class_scope:google.iam.credentials.v1.GenerateIdentityBindingAccessTokenResponse)
    ),
)
_sym_db.RegisterMessage(GenerateIdentityBindingAccessTokenResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n#com.google.cloud.iam.credentials.v1B\031IAMCredentialsCommonProtoP\001ZDgoogle.golang.org/genproto/googleapis/iam/credentials/v1;credentials\370\001\001"
    ),
)
# @@protoc_insertion_point(module_scope)
