# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: policy.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from google.protobuf.empty_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpolicy.proto\x12\x06policy\x1a\x1bgoogle/protobuf/empty.proto\"\x1f\n\x0eHealthCheckReq\x12\r\n\x05nonce\x18\x01 \x01(\x05\"\"\n\x10HealthCheckReply\x12\x0e\n\x06Retval\x18\x01 \x01(\x05\"0\n\x08response\x12$\n\x06status\x18\x01 \x01(\x0e\x32\x14.policy.PolicyStatus\"\x18\n\x06policy\x12\x0e\n\x06policy\x18\x01 \x01(\x0c\":\n\rContainerData\x12\x12\n\npolicyList\x18\x01 \x03(\t\x12\x15\n\rpolicyEnabled\x18\x02 \x01(\x05\"*\n\x14HostSecurityPolicies\x12\x12\n\npolicyList\x18\x01 \x03(\t\"\xb4\x02\n\rProbeResponse\x12\x15\n\rcontainerList\x18\x01 \x03(\t\x12=\n\x0c\x63ontainerMap\x18\x02 \x03(\x0b\x32\'.policy.ProbeResponse.ContainerMapEntry\x12\x33\n\x07hostMap\x18\x03 \x03(\x0b\x32\".policy.ProbeResponse.HostMapEntry\x1aJ\n\x11\x43ontainerMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.policy.ContainerData:\x02\x38\x01\x1aL\n\x0cHostMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.policy.HostSecurityPolicies:\x02\x38\x01*^\n\x0cPolicyStatus\x12\x0b\n\x07\x46\x61ilure\x10\x00\x12\x0b\n\x07\x41pplied\x10\x01\x12\x0b\n\x07\x44\x65leted\x10\x02\x12\x0c\n\x08Modified\x10\x03\x12\x0c\n\x08NotExist\x10\x04\x12\x0b\n\x07Invalid\x10\x05\x32M\n\x0cProbeService\x12=\n\x0cgetProbeData\x12\x16.google.protobuf.Empty\x1a\x15.policy.ProbeResponse2t\n\rPolicyService\x12\x33\n\x0f\x63ontainerPolicy\x12\x0e.policy.policy\x1a\x10.policy.response\x12.\n\nhostPolicy\x12\x0e.policy.policy\x1a\x10.policy.response2\xc3\x01\n\x13PolicyStreamService\x12?\n\x0bHealthCheck\x12\x16.policy.HealthCheckReq\x1a\x18.policy.HealthCheckReply\x12\x37\n\x0f\x63ontainerPolicy\x12\x10.policy.response\x1a\x0e.policy.policy(\x01\x30\x01\x12\x32\n\nhostPolicy\x12\x10.policy.response\x1a\x0e.policy.policy(\x01\x30\x01\x42)Z\'github.com/kubearmor/KubeArmor/protobufP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'policy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/kubearmor/KubeArmor/protobuf'
  _globals['_PROBERESPONSE_CONTAINERMAPENTRY']._options = None
  _globals['_PROBERESPONSE_CONTAINERMAPENTRY']._serialized_options = b'8\001'
  _globals['_PROBERESPONSE_HOSTMAPENTRY']._options = None
  _globals['_PROBERESPONSE_HOSTMAPENTRY']._serialized_options = b'8\001'
  _globals['_POLICYSTATUS']._serialized_start=613
  _globals['_POLICYSTATUS']._serialized_end=707
  _globals['_HEALTHCHECKREQ']._serialized_start=53
  _globals['_HEALTHCHECKREQ']._serialized_end=84
  _globals['_HEALTHCHECKREPLY']._serialized_start=86
  _globals['_HEALTHCHECKREPLY']._serialized_end=120
  _globals['_RESPONSE']._serialized_start=122
  _globals['_RESPONSE']._serialized_end=170
  _globals['_POLICY']._serialized_start=172
  _globals['_POLICY']._serialized_end=196
  _globals['_CONTAINERDATA']._serialized_start=198
  _globals['_CONTAINERDATA']._serialized_end=256
  _globals['_HOSTSECURITYPOLICIES']._serialized_start=258
  _globals['_HOSTSECURITYPOLICIES']._serialized_end=300
  _globals['_PROBERESPONSE']._serialized_start=303
  _globals['_PROBERESPONSE']._serialized_end=611
  _globals['_PROBERESPONSE_CONTAINERMAPENTRY']._serialized_start=459
  _globals['_PROBERESPONSE_CONTAINERMAPENTRY']._serialized_end=533
  _globals['_PROBERESPONSE_HOSTMAPENTRY']._serialized_start=535
  _globals['_PROBERESPONSE_HOSTMAPENTRY']._serialized_end=611
  _globals['_PROBESERVICE']._serialized_start=709
  _globals['_PROBESERVICE']._serialized_end=786
  _globals['_POLICYSERVICE']._serialized_start=788
  _globals['_POLICYSERVICE']._serialized_end=904
  _globals['_POLICYSTREAMSERVICE']._serialized_start=907
  _globals['_POLICYSTREAMSERVICE']._serialized_end=1102
# @@protoc_insertion_point(module_scope)
