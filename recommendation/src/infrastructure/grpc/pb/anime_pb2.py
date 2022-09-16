# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anime.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61nime.proto\x12\x05\x61nime\"\xc3\x02\n\x05\x41nime\x12\x0e\n\x06mal_id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x0e\n\x06genres\x18\x04 \x01(\t\x12\x15\n\rjapanese_name\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x10\n\x08\x65pisodes\x18\x07 \x01(\r\x12\x1c\n\x14\x62roadcast_start_date\x18\x08 \x01(\t\x12\x1a\n\x12\x62roadcast_end_date\x18\t \x01(\t\x12\x17\n\x0fseason_premiere\x18\n \x01(\t\x12\x0f\n\x07studios\x18\x0b \x01(\t\x12\x0e\n\x06source\x18\x0c \x01(\t\x12\x1a\n\x12\x61ge_classification\x18\r \x01(\t\x12\x12\n\npopularity\x18\x0e \x01(\r\x12\x10\n\x08watching\x18\x0f \x01(\r\x12\x10\n\x08synopsis\x18\x10 \x01(\t\"p\n\x0b\x41nimeRating\x12\x0f\n\x07user_id\x18\x01 \x01(\r\x12\x10\n\x08\x61nime_id\x18\x02 \x01(\r\x12\x0e\n\x06rating\x18\x03 \x01(\r\x12.\n\x0fwatching_status\x18\x04 \x01(\x0e\x32\x15.anime.WatchingStatus\"\x06\n\x04Void*q\n\x0eWatchingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x16\n\x12\x43URRENTLY_WATCHING\x10\x01\x12\r\n\tCOMPLETED\x10\x02\x12\x0b\n\x07ON_HOLD\x10\x03\x12\x0b\n\x07\x44ROPPED\x10\x04\x12\x11\n\rPLAN_TO_WATCH\x10\x05\x32t\n\x0c\x41nimeService\x12+\n\nFetchAnime\x12\x0c.anime.Anime\x1a\x0b.anime.Void\"\x00(\x01\x12\x37\n\x10\x46\x65tchAnimeRating\x12\x12.anime.AnimeRating\x1a\x0b.anime.Void\"\x00(\x01\x62\x06proto3')

_WATCHINGSTATUS = DESCRIPTOR.enum_types_by_name['WatchingStatus']
WatchingStatus = enum_type_wrapper.EnumTypeWrapper(_WATCHINGSTATUS)
UNKNOWN = 0
CURRENTLY_WATCHING = 1
COMPLETED = 2
ON_HOLD = 3
DROPPED = 4
PLAN_TO_WATCH = 5


_ANIME = DESCRIPTOR.message_types_by_name['Anime']
_ANIMERATING = DESCRIPTOR.message_types_by_name['AnimeRating']
_VOID = DESCRIPTOR.message_types_by_name['Void']
Anime = _reflection.GeneratedProtocolMessageType('Anime', (_message.Message,), {
  'DESCRIPTOR' : _ANIME,
  '__module__' : 'anime_pb2'
  # @@protoc_insertion_point(class_scope:anime.Anime)
  })
_sym_db.RegisterMessage(Anime)

AnimeRating = _reflection.GeneratedProtocolMessageType('AnimeRating', (_message.Message,), {
  'DESCRIPTOR' : _ANIMERATING,
  '__module__' : 'anime_pb2'
  # @@protoc_insertion_point(class_scope:anime.AnimeRating)
  })
_sym_db.RegisterMessage(AnimeRating)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'anime_pb2'
  # @@protoc_insertion_point(class_scope:anime.Void)
  })
_sym_db.RegisterMessage(Void)

_ANIMESERVICE = DESCRIPTOR.services_by_name['AnimeService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WATCHINGSTATUS._serialized_start=470
  _WATCHINGSTATUS._serialized_end=583
  _ANIME._serialized_start=23
  _ANIME._serialized_end=346
  _ANIMERATING._serialized_start=348
  _ANIMERATING._serialized_end=460
  _VOID._serialized_start=462
  _VOID._serialized_end=468
  _ANIMESERVICE._serialized_start=585
  _ANIMESERVICE._serialized_end=701
# @@protoc_insertion_point(module_scope)
