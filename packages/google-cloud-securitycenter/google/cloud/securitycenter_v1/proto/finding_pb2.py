# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter_v1/proto/finding.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.securitycenter_v1.proto import (
    security_marks_pb2 as google_dot_cloud_dot_securitycenter__v1_dot_proto_dot_security__marks__pb2,
)
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/securitycenter_v1/proto/finding.proto",
    package="google.cloud.securitycenter.v1",
    syntax="proto3",
    serialized_options=_b(
        '\n"com.google.cloud.securitycenter.v1P\001ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\252\002\036Google.Cloud.SecurityCenter.V1\312\002\036Google\\Cloud\\SecurityCenter\\V1\352\002!Google::Cloud::SecurityCenter::V1'
    ),
    serialized_pb=_b(
        '\n2google/cloud/securitycenter_v1/proto/finding.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x39google/cloud/securitycenter_v1/proto/security_marks.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\x04\n\x07\x46inding\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x15\n\rresource_name\x18\x03 \x01(\t\x12<\n\x05state\x18\x04 \x01(\x0e\x32-.google.cloud.securitycenter.v1.Finding.State\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\x14\n\x0c\x65xternal_uri\x18\x06 \x01(\t\x12X\n\x11source_properties\x18\x07 \x03(\x0b\x32=.google.cloud.securitycenter.v1.Finding.SourcePropertiesEntry\x12\x45\n\x0esecurity_marks\x18\x08 \x01(\x0b\x32-.google.cloud.securitycenter.v1.SecurityMarks\x12.\n\nevent_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x63reate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1aO\n\x15SourcePropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01"8\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x42\xda\x01\n"com.google.cloud.securitycenter.v1P\x01ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_securitycenter__v1_dot_proto_dot_security__marks__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_FINDING_STATE = _descriptor.EnumDescriptor(
    name="State",
    full_name="google.cloud.securitycenter.v1.Finding.State",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STATE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACTIVE", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INACTIVE", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=744,
    serialized_end=800,
)
_sym_db.RegisterEnumDescriptor(_FINDING_STATE)


_FINDING_SOURCEPROPERTIESENTRY = _descriptor.Descriptor(
    name="SourcePropertiesEntry",
    full_name="google.cloud.securitycenter.v1.Finding.SourcePropertiesEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.securitycenter.v1.Finding.SourcePropertiesEntry.key",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.securitycenter.v1.Finding.SourcePropertiesEntry.value",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=663,
    serialized_end=742,
)

_FINDING = _descriptor.Descriptor(
    name="Finding",
    full_name="google.cloud.securitycenter.v1.Finding",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.securitycenter.v1.Finding.name",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.securitycenter.v1.Finding.parent",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="resource_name",
            full_name="google.cloud.securitycenter.v1.Finding.resource_name",
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="state",
            full_name="google.cloud.securitycenter.v1.Finding.state",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="category",
            full_name="google.cloud.securitycenter.v1.Finding.category",
            index=4,
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="external_uri",
            full_name="google.cloud.securitycenter.v1.Finding.external_uri",
            index=5,
            number=6,
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="source_properties",
            full_name="google.cloud.securitycenter.v1.Finding.source_properties",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="security_marks",
            full_name="google.cloud.securitycenter.v1.Finding.security_marks",
            index=7,
            number=8,
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="event_time",
            full_name="google.cloud.securitycenter.v1.Finding.event_time",
            index=8,
            number=9,
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.securitycenter.v1.Finding.create_time",
            index=9,
            number=10,
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
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_FINDING_SOURCEPROPERTIESENTRY,],
    enum_types=[_FINDING_STATE,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=239,
    serialized_end=800,
)

_FINDING_SOURCEPROPERTIESENTRY.fields_by_name[
    "value"
].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FINDING_SOURCEPROPERTIESENTRY.containing_type = _FINDING
_FINDING.fields_by_name["state"].enum_type = _FINDING_STATE
_FINDING.fields_by_name[
    "source_properties"
].message_type = _FINDING_SOURCEPROPERTIESENTRY
_FINDING.fields_by_name[
    "security_marks"
].message_type = (
    google_dot_cloud_dot_securitycenter__v1_dot_proto_dot_security__marks__pb2._SECURITYMARKS
)
_FINDING.fields_by_name[
    "event_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FINDING.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FINDING_STATE.containing_type = _FINDING
DESCRIPTOR.message_types_by_name["Finding"] = _FINDING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Finding = _reflection.GeneratedProtocolMessageType(
    "Finding",
    (_message.Message,),
    dict(
        SourcePropertiesEntry=_reflection.GeneratedProtocolMessageType(
            "SourcePropertiesEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_FINDING_SOURCEPROPERTIESENTRY,
                __module__="google.cloud.securitycenter_v1.proto.finding_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.Finding.SourcePropertiesEntry)
            ),
        ),
        DESCRIPTOR=_FINDING,
        __module__="google.cloud.securitycenter_v1.proto.finding_pb2",
        __doc__="""Cloud Security Command Center (Cloud SCC) finding.
  
  A finding is a record of assessment data (security, risk, health or
  privacy) ingested into Cloud SCC for presentation, notification,
  analysis, policy testing, and enforcement. For example, an XSS
  vulnerability in an App Engine application is a finding.
  
  
  Attributes:
      name:
          The relative resource name of this finding. See: https://cloud
          .google.com/apis/design/resource\_names#relative\_resource\_na
          me Example: "organizations/123/sources/456/findings/789"
      parent:
          The relative resource name of the source the finding belongs
          to. See: https://cloud.google.com/apis/design/resource\_names#
          relative\_resource\_name This field is immutable after
          creation time. For example: "organizations/123/sources/456"
      resource_name:
          The full resource name of the Google Cloud Platform (GCP)
          resource this finding is for. See: https://cloud.google.com/ap
          is/design/resource\_names#full\_resource\_name This field is
          immutable after creation time.
      state:
          The state of the finding.
      category:
          The additional taxonomy group within findings from a given
          source. This field is immutable after creation time. Example:
          "XSS\_FLASH\_INJECTION"
      external_uri:
          The URI that, if available, points to a web page outside of
          Cloud SCC where additional information about the finding can
          be found. This field is guaranteed to be either empty or a
          well formed URL.
      source_properties:
          Source specific properties. These properties are managed by
          the source that writes the finding. The key names in the
          source\_properties map must be between 1 and 255 characters,
          and must start with a letter and contain alphanumeric
          characters or underscores only.
      security_marks:
          Output only. User specified security marks. These marks are
          entirely managed by the user and come from the SecurityMarks
          resource that belongs to the finding.
      event_time:
          The time at which the event took place. For example, if the
          finding represents an open firewall it would capture the time
          the open firewall was detected.
      create_time:
          The time at which the finding was created in Cloud SCC.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.Finding)
    ),
)
_sym_db.RegisterMessage(Finding)
_sym_db.RegisterMessage(Finding.SourcePropertiesEntry)


DESCRIPTOR._options = None
_FINDING_SOURCEPROPERTIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
