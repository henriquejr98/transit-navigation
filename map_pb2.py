# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tmap.proto\x12\x0bvector_tile\"\xd1\x04\n\x04Tile\x12\'\n\x06layers\x18\x03 \x03(\x0b\x32\x17.vector_tile.Tile.Layer\x1a\xa1\x01\n\x05Value\x12\x14\n\x0cstring_value\x18\x01 \x01(\t\x12\x13\n\x0b\x66loat_value\x18\x02 \x01(\x02\x12\x14\n\x0c\x64ouble_value\x18\x03 \x01(\x01\x12\x11\n\tint_value\x18\x04 \x01(\x03\x12\x12\n\nuint_value\x18\x05 \x01(\x04\x12\x12\n\nsint_value\x18\x06 \x01(\x12\x12\x12\n\nbool_value\x18\x07 \x01(\x08*\x08\x08\x08\x10\x80\x80\x80\x80\x02\x1a\x83\x01\n\x07\x46\x65\x61ture\x12\r\n\x02id\x18\x01 \x01(\x04:\x01\x30\x12\x10\n\x04tags\x18\x02 \x03(\rB\x02\x10\x01\x12\x31\n\x04type\x18\x03 \x01(\x0e\x32\x1a.vector_tile.Tile.GeomType:\x07UNKNOWN\x12\x14\n\x08geometry\x18\x04 \x03(\rB\x02\x10\x01\x12\x0e\n\x06raster\x18\x05 \x01(\x0c\x1a\xad\x01\n\x05Layer\x12\x12\n\x07version\x18\x0f \x02(\r:\x01\x31\x12\x0c\n\x04name\x18\x01 \x02(\t\x12+\n\x08\x66\x65\x61tures\x18\x02 \x03(\x0b\x32\x19.vector_tile.Tile.Feature\x12\x0c\n\x04keys\x18\x03 \x03(\t\x12\'\n\x06values\x18\x04 \x03(\x0b\x32\x17.vector_tile.Tile.Value\x12\x14\n\x06\x65xtent\x18\x05 \x01(\r:\x04\x34\x30\x39\x36*\x08\x08\x10\x10\x80\x80\x80\x80\x02\"?\n\x08GeomType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05POINT\x10\x01\x12\x0e\n\nLINESTRING\x10\x02\x12\x0b\n\x07POLYGON\x10\x03*\x05\x08\x10\x10\x80@B\x02H\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'map_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003'
  _TILE_FEATURE.fields_by_name['tags']._options = None
  _TILE_FEATURE.fields_by_name['tags']._serialized_options = b'\020\001'
  _TILE_FEATURE.fields_by_name['geometry']._options = None
  _TILE_FEATURE.fields_by_name['geometry']._serialized_options = b'\020\001'
  _globals['_TILE']._serialized_start=27
  _globals['_TILE']._serialized_end=620
  _globals['_TILE_VALUE']._serialized_start=77
  _globals['_TILE_VALUE']._serialized_end=238
  _globals['_TILE_FEATURE']._serialized_start=241
  _globals['_TILE_FEATURE']._serialized_end=372
  _globals['_TILE_LAYER']._serialized_start=375
  _globals['_TILE_LAYER']._serialized_end=548
  _globals['_TILE_GEOMTYPE']._serialized_start=550
  _globals['_TILE_GEOMTYPE']._serialized_end=613
# @@protoc_insertion_point(module_scope)
