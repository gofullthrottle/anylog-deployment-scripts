# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kvm.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tkvm.proto\x12\x03kvm\"!\n\ragentIdentity\x12\x10\n\x08identity\x18\x01 \x01(\t\"\x18\n\x06status\x12\x0e\n\x06status\x18\x01 \x01(\x05\" \n\npolicyData\x12\x12\n\npolicyData\x18\x01 \x01(\x0c\x32o\n\x03KVM\x12\x38\n\x15registerAgentIdentity\x12\x12.kvm.agentIdentity\x1a\x0b.kvm.status\x12.\n\nsendPolicy\x12\x0b.kvm.status\x1a\x0f.kvm.policyData(\x01\x30\x01\x42)Z\'github.com/kubearmor/KubeArmor/protobufb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kvm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/kubearmor/KubeArmor/protobuf'
  _globals['_AGENTIDENTITY']._serialized_start=18
  _globals['_AGENTIDENTITY']._serialized_end=51
  _globals['_STATUS']._serialized_start=53
  _globals['_STATUS']._serialized_end=77
  _globals['_POLICYDATA']._serialized_start=79
  _globals['_POLICYDATA']._serialized_end=111
  _globals['_KVM']._serialized_start=113
  _globals['_KVM']._serialized_end=224
# @@protoc_insertion_point(module_scope)
