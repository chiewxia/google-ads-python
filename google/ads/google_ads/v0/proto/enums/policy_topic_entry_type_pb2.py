# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/policy_topic_entry_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/policy_topic_entry_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\nAgoogle/ads/googleads_v0/proto/enums/policy_topic_entry_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\xaa\x01\n\x18PolicyTopicEntryTypeEnum\"\x8d\x01\n\x14PolicyTopicEntryType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0e\n\nPROHIBITED\x10\x02\x12\x0b\n\x07LIMITED\x10\x04\x12\x0f\n\x0b\x44\x45SCRIPTIVE\x10\x05\x12\x0e\n\nBROADENING\x10\x06\x12\x19\n\x15\x41REA_OF_INTEREST_ONLY\x10\x07\x42\xca\x01\n!com.google.ads.googleads.v0.enumsB\x19PolicyTopicEntryTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_POLICYTOPICENTRYTYPEENUM_POLICYTOPICENTRYTYPE = _descriptor.EnumDescriptor(
  name='PolicyTopicEntryType',
  full_name='google.ads.googleads.v0.enums.PolicyTopicEntryTypeEnum.PolicyTopicEntryType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIMITED', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTIVE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROADENING', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AREA_OF_INTEREST_ONLY', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=130,
  serialized_end=271,
)
_sym_db.RegisterEnumDescriptor(_POLICYTOPICENTRYTYPEENUM_POLICYTOPICENTRYTYPE)


_POLICYTOPICENTRYTYPEENUM = _descriptor.Descriptor(
  name='PolicyTopicEntryTypeEnum',
  full_name='google.ads.googleads.v0.enums.PolicyTopicEntryTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POLICYTOPICENTRYTYPEENUM_POLICYTOPICENTRYTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=271,
)

_POLICYTOPICENTRYTYPEENUM_POLICYTOPICENTRYTYPE.containing_type = _POLICYTOPICENTRYTYPEENUM
DESCRIPTOR.message_types_by_name['PolicyTopicEntryTypeEnum'] = _POLICYTOPICENTRYTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PolicyTopicEntryTypeEnum = _reflection.GeneratedProtocolMessageType('PolicyTopicEntryTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _POLICYTOPICENTRYTYPEENUM,
  __module__ = 'google.ads.google_ads.v0.proto.enums.policy_topic_entry_type_pb2'
  ,
  __doc__ = """Container for enum describing possible policy topic entry types.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.PolicyTopicEntryTypeEnum)
  ))
_sym_db.RegisterMessage(PolicyTopicEntryTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\031PolicyTopicEntryTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
