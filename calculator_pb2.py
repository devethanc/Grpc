# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: calculator.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'calculator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\x12\ncalculator\"\"\n\nSumRequest\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\"\x1d\n\x0bSumResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32\x44\n\nCalculator\x12\x36\n\x03Sum\x12\x16.calculator.SumRequest\x1a\x17.calculator.SumResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SUMREQUEST']._serialized_start=32
  _globals['_SUMREQUEST']._serialized_end=66
  _globals['_SUMRESPONSE']._serialized_start=68
  _globals['_SUMRESPONSE']._serialized_end=97
  _globals['_CALCULATOR']._serialized_start=99
  _globals['_CALCULATOR']._serialized_end=167
# @@protoc_insertion_point(module_scope)
