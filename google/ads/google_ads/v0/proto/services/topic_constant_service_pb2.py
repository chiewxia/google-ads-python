# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/topic_constant_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import topic_constant_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_topic__constant__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/topic_constant_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\nCgoogle/ads/googleads_v0/proto/services/topic_constant_service.proto\x12 google.ads.googleads.v0.services\x1a<google/ads/googleads_v0/proto/resources/topic_constant.proto\x1a\x1cgoogle/api/annotations.proto\"0\n\x17GetTopicConstantRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xc6\x01\n\x14TopicConstantService\x12\xad\x01\n\x10GetTopicConstant\x12\x39.google.ads.googleads.v0.services.GetTopicConstantRequest\x1a\x30.google.ads.googleads.v0.resources.TopicConstant\",\x82\xd3\xe4\x93\x02&\x12$/v0/{resource_name=topicConstants/*}B\xd9\x01\n$com.google.ads.googleads.v0.servicesB\x19TopicConstantServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_topic__constant__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETTOPICCONSTANTREQUEST = _descriptor.Descriptor(
  name='GetTopicConstantRequest',
  full_name='google.ads.googleads.v0.services.GetTopicConstantRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetTopicConstantRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=245,
)

DESCRIPTOR.message_types_by_name['GetTopicConstantRequest'] = _GETTOPICCONSTANTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTopicConstantRequest = _reflection.GeneratedProtocolMessageType('GetTopicConstantRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTOPICCONSTANTREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.topic_constant_service_pb2'
  ,
  __doc__ = """Request message for
  [TopicConstantService.GetTopicConstant][google.ads.googleads.v0.services.TopicConstantService.GetTopicConstant].
  
  
  Attributes:
      resource_name:
          Resource name of the Topic to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetTopicConstantRequest)
  ))
_sym_db.RegisterMessage(GetTopicConstantRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\031TopicConstantServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_TOPICCONSTANTSERVICE = _descriptor.ServiceDescriptor(
  name='TopicConstantService',
  full_name='google.ads.googleads.v0.services.TopicConstantService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=248,
  serialized_end=446,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTopicConstant',
    full_name='google.ads.googleads.v0.services.TopicConstantService.GetTopicConstant',
    index=0,
    containing_service=None,
    input_type=_GETTOPICCONSTANTREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_topic__constant__pb2._TOPICCONSTANT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002&\022$/v0/{resource_name=topicConstants/*}')),
  ),
])
_sym_db.RegisterServiceDescriptor(_TOPICCONSTANTSERVICE)

DESCRIPTOR.services_by_name['TopicConstantService'] = _TOPICCONSTANTSERVICE

# @@protoc_insertion_point(module_scope)
