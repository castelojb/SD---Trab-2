# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Protobuffer/messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Protobuffer/messages.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aProtobuffer/messages.proto\x1a\x1bgoogle/protobuf/empty.proto\"(\n\x0b\x46\x65tchStatus\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.StatusType\"\x13\n\x02Id\x12\r\n\x05value\x18\x01 \x01(\t\"V\n\x0eIdentification\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1c\n\x04type\x18\x02 \x01(\x0e\x32\x0e.EquipmentType\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\"@\n\x06Status\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.StatusType\x12\x0f\n\x07payload\x18\x02 \x01(\x01\x12\n\n\x02id\x18\x03 \x01(\t\":\n\x0cUpdateStatus\x12\x19\n\x04type\x18\t \x01(\x0e\x32\x0b.StatusType\x12\x0f\n\x07payload\x18\n \x01(\x01*3\n\rEquipmentType\x12\x08\n\x04\x42OTH\x10\x00\x12\n\n\x06SENSOR\x10\x01\x12\x0c\n\x08\x41\x43TUATOR\x10\x02*.\n\nStatusType\x12\x0f\n\x0bTURN_ON_OFF\x10\x00\x12\x0f\n\x0bTEMPERATURE\x10\x01\x32Y\n\x0eGatewayService\x12$\n\x0cIdentificate\x12\x0f.Identification\x1a\x03.Id\x12!\n\rReceiveStatus\x12\x07.Status\x1a\x07.Status2\xa7\x01\n\x10\x45quipmentService\x12\x37\n\x0cIdentificate\x12\x16.google.protobuf.Empty\x1a\x0f.Identification\x12\x36\n\rReceiveUpdate\x12\r.UpdateStatus\x1a\x16.google.protobuf.Empty\x12\"\n\tGetStatus\x12\x0c.FetchStatus\x1a\x07.Statusb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_EQUIPMENTTYPE = _descriptor.EnumDescriptor(
  name='EquipmentType',
  full_name='EquipmentType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOTH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTUATOR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=336,
  serialized_end=387,
)
_sym_db.RegisterEnumDescriptor(_EQUIPMENTTYPE)

EquipmentType = enum_type_wrapper.EnumTypeWrapper(_EQUIPMENTTYPE)
_STATUSTYPE = _descriptor.EnumDescriptor(
  name='StatusType',
  full_name='StatusType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TURN_ON_OFF', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEMPERATURE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=389,
  serialized_end=435,
)
_sym_db.RegisterEnumDescriptor(_STATUSTYPE)

StatusType = enum_type_wrapper.EnumTypeWrapper(_STATUSTYPE)
BOTH = 0
SENSOR = 1
ACTUATOR = 2
TURN_ON_OFF = 0
TEMPERATURE = 1



_FETCHSTATUS = _descriptor.Descriptor(
  name='FetchStatus',
  full_name='FetchStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='FetchStatus.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=99,
)


_ID = _descriptor.Descriptor(
  name='Id',
  full_name='Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Id.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=120,
)


_IDENTIFICATION = _descriptor.Descriptor(
  name='Identification',
  full_name='Identification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Identification.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Identification.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='Identification.ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='Identification.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=208,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Status.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='Status.payload', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Status.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=274,
)


_UPDATESTATUS = _descriptor.Descriptor(
  name='UpdateStatus',
  full_name='UpdateStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='UpdateStatus.type', index=0,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='UpdateStatus.payload', index=1,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=334,
)

_FETCHSTATUS.fields_by_name['type'].enum_type = _STATUSTYPE
_IDENTIFICATION.fields_by_name['type'].enum_type = _EQUIPMENTTYPE
_STATUS.fields_by_name['type'].enum_type = _STATUSTYPE
_UPDATESTATUS.fields_by_name['type'].enum_type = _STATUSTYPE
DESCRIPTOR.message_types_by_name['FetchStatus'] = _FETCHSTATUS
DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['Identification'] = _IDENTIFICATION
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['UpdateStatus'] = _UPDATESTATUS
DESCRIPTOR.enum_types_by_name['EquipmentType'] = _EQUIPMENTTYPE
DESCRIPTOR.enum_types_by_name['StatusType'] = _STATUSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FetchStatus = _reflection.GeneratedProtocolMessageType('FetchStatus', (_message.Message,), {
  'DESCRIPTOR' : _FETCHSTATUS,
  '__module__' : 'Protobuffer.messages_pb2'
  # @@protoc_insertion_point(class_scope:FetchStatus)
  })
_sym_db.RegisterMessage(FetchStatus)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'Protobuffer.messages_pb2'
  # @@protoc_insertion_point(class_scope:Id)
  })
_sym_db.RegisterMessage(Id)

Identification = _reflection.GeneratedProtocolMessageType('Identification', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFICATION,
  '__module__' : 'Protobuffer.messages_pb2'
  # @@protoc_insertion_point(class_scope:Identification)
  })
_sym_db.RegisterMessage(Identification)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'Protobuffer.messages_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  })
_sym_db.RegisterMessage(Status)

UpdateStatus = _reflection.GeneratedProtocolMessageType('UpdateStatus', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTATUS,
  '__module__' : 'Protobuffer.messages_pb2'
  # @@protoc_insertion_point(class_scope:UpdateStatus)
  })
_sym_db.RegisterMessage(UpdateStatus)



_GATEWAYSERVICE = _descriptor.ServiceDescriptor(
  name='GatewayService',
  full_name='GatewayService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=437,
  serialized_end=526,
  methods=[
  _descriptor.MethodDescriptor(
    name='Identificate',
    full_name='GatewayService.Identificate',
    index=0,
    containing_service=None,
    input_type=_IDENTIFICATION,
    output_type=_ID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReceiveStatus',
    full_name='GatewayService.ReceiveStatus',
    index=1,
    containing_service=None,
    input_type=_STATUS,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAYSERVICE)

DESCRIPTOR.services_by_name['GatewayService'] = _GATEWAYSERVICE


_EQUIPMENTSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentService',
  full_name='EquipmentService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=529,
  serialized_end=696,
  methods=[
  _descriptor.MethodDescriptor(
    name='Identificate',
    full_name='EquipmentService.Identificate',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_IDENTIFICATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReceiveUpdate',
    full_name='EquipmentService.ReceiveUpdate',
    index=1,
    containing_service=None,
    input_type=_UPDATESTATUS,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='EquipmentService.GetStatus',
    index=2,
    containing_service=None,
    input_type=_FETCHSTATUS,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTSERVICE)

DESCRIPTOR.services_by_name['EquipmentService'] = _EQUIPMENTSERVICE

# @@protoc_insertion_point(module_scope)
