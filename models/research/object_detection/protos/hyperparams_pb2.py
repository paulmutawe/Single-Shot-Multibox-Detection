# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/hyperparams.proto
# Protobuf Python Version: 5.29.2
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
    2,
    '',
    'object_detection/protos/hyperparams.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)object_detection/protos/hyperparams.proto\x12\x17object_detection.protos\"\xe5\x04\n\x0bHyperparams\x12\x39\n\x02op\x18\x01 \x01(\x0e\x32\'.object_detection.protos.Hyperparams.Op:\x04\x43ONV\x12\x39\n\x0bregularizer\x18\x02 \x01(\x0b\x32$.object_detection.protos.Regularizer\x12\x39\n\x0binitializer\x18\x03 \x01(\x0b\x32$.object_detection.protos.Initializer\x12I\n\nactivation\x18\x04 \x01(\x0e\x32/.object_detection.protos.Hyperparams.Activation:\x04RELU\x12\x38\n\nbatch_norm\x18\x05 \x01(\x0b\x32\".object_detection.protos.BatchNormH\x00\x12=\n\x0fsync_batch_norm\x18\t \x01(\x0b\x32\".object_detection.protos.BatchNormH\x00\x12\x38\n\ngroup_norm\x18\x07 \x01(\x0b\x32\".object_detection.protos.GroupNormH\x00\x12#\n\x14regularize_depthwise\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x0e\x66orce_use_bias\x18\x08 \x01(\x08:\x05\x66\x61lse\"\x16\n\x02Op\x12\x08\n\x04\x43ONV\x10\x01\x12\x06\n\x02\x46\x43\x10\x02\"7\n\nActivation\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04RELU\x10\x01\x12\n\n\x06RELU_6\x10\x02\x12\t\n\x05SWISH\x10\x03\x42\x12\n\x10normalizer_oneof\"\xa6\x01\n\x0bRegularizer\x12@\n\x0el1_regularizer\x18\x01 \x01(\x0b\x32&.object_detection.protos.L1RegularizerH\x00\x12@\n\x0el2_regularizer\x18\x02 \x01(\x0b\x32&.object_detection.protos.L2RegularizerH\x00\x42\x13\n\x11regularizer_oneof\"\"\n\rL1Regularizer\x12\x11\n\x06weight\x18\x01 \x01(\x02:\x01\x31\"\"\n\rL2Regularizer\x12\x11\n\x06weight\x18\x01 \x01(\x02:\x01\x31\"\xd8\x02\n\x0bInitializer\x12[\n\x1ctruncated_normal_initializer\x18\x01 \x01(\x0b\x32\x33.object_detection.protos.TruncatedNormalInitializerH\x00\x12[\n\x1cvariance_scaling_initializer\x18\x02 \x01(\x0b\x32\x33.object_detection.protos.VarianceScalingInitializerH\x00\x12U\n\x19random_normal_initializer\x18\x03 \x01(\x0b\x32\x30.object_detection.protos.RandomNormalInitializerH\x00\x12#\n\x19keras_initializer_by_name\x18\x04 \x01(\tH\x00\x42\x13\n\x11initializer_oneof\"@\n\x1aTruncatedNormalInitializer\x12\x0f\n\x04mean\x18\x01 \x01(\x02:\x01\x30\x12\x11\n\x06stddev\x18\x02 \x01(\x02:\x01\x31\"\xc5\x01\n\x1aVarianceScalingInitializer\x12\x11\n\x06\x66\x61\x63tor\x18\x01 \x01(\x02:\x01\x32\x12\x16\n\x07uniform\x18\x02 \x01(\x08:\x05\x66\x61lse\x12N\n\x04mode\x18\x03 \x01(\x0e\x32\x38.object_detection.protos.VarianceScalingInitializer.Mode:\x06\x46\x41N_IN\",\n\x04Mode\x12\n\n\x06\x46\x41N_IN\x10\x00\x12\x0b\n\x07\x46\x41N_OUT\x10\x01\x12\x0b\n\x07\x46\x41N_AVG\x10\x02\"=\n\x17RandomNormalInitializer\x12\x0f\n\x04mean\x18\x01 \x01(\x02:\x01\x30\x12\x11\n\x06stddev\x18\x02 \x01(\x02:\x01\x31\"z\n\tBatchNorm\x12\x14\n\x05\x64\x65\x63\x61y\x18\x01 \x01(\x02:\x05\x30.999\x12\x14\n\x06\x63\x65nter\x18\x02 \x01(\x08:\x04true\x12\x14\n\x05scale\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07\x65psilon\x18\x04 \x01(\x02:\x05\x30.001\x12\x13\n\x05train\x18\x05 \x01(\x08:\x04true\"\x0b\n\tGroupNorm')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.hyperparams_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HYPERPARAMS']._serialized_start=71
  _globals['_HYPERPARAMS']._serialized_end=684
  _globals['_HYPERPARAMS_OP']._serialized_start=585
  _globals['_HYPERPARAMS_OP']._serialized_end=607
  _globals['_HYPERPARAMS_ACTIVATION']._serialized_start=609
  _globals['_HYPERPARAMS_ACTIVATION']._serialized_end=664
  _globals['_REGULARIZER']._serialized_start=687
  _globals['_REGULARIZER']._serialized_end=853
  _globals['_L1REGULARIZER']._serialized_start=855
  _globals['_L1REGULARIZER']._serialized_end=889
  _globals['_L2REGULARIZER']._serialized_start=891
  _globals['_L2REGULARIZER']._serialized_end=925
  _globals['_INITIALIZER']._serialized_start=928
  _globals['_INITIALIZER']._serialized_end=1272
  _globals['_TRUNCATEDNORMALINITIALIZER']._serialized_start=1274
  _globals['_TRUNCATEDNORMALINITIALIZER']._serialized_end=1338
  _globals['_VARIANCESCALINGINITIALIZER']._serialized_start=1341
  _globals['_VARIANCESCALINGINITIALIZER']._serialized_end=1538
  _globals['_VARIANCESCALINGINITIALIZER_MODE']._serialized_start=1494
  _globals['_VARIANCESCALINGINITIALIZER_MODE']._serialized_end=1538
  _globals['_RANDOMNORMALINITIALIZER']._serialized_start=1540
  _globals['_RANDOMNORMALINITIALIZER']._serialized_end=1601
  _globals['_BATCHNORM']._serialized_start=1603
  _globals['_BATCHNORM']._serialized_end=1725
  _globals['_GROUPNORM']._serialized_start=1727
  _globals['_GROUPNORM']._serialized_end=1738
# @@protoc_insertion_point(module_scope)
