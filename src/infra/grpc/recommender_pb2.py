# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommender.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11recommender.proto\x12\x0brecommender":\n\x0eRecommendation\x12\x1a\n\x12recommendedAnimeId\x18\x01 \x01(\x05\x12\x0c\n\x04rank\x18\x02 \x01(\x05"\x07\n\x05\x45mpty"$\n\x11IsTrainedResponse\x12\x0f\n\x07trained\x18\x01 \x01(\x08"X\n\x15RecommendationRequest\x12\x0f\n\x07\x61nimeId\x18\x01 \x01(\x05\x12\x0e\n\x01k\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x10\x65xcludedAnimeIds\x18\x03 \x03(\x05\x42\x04\n\x02_k"_\n\x16RecommendationResponse\x12\x0f\n\x07\x61nimeId\x18\x01 \x01(\x05\x12\x34\n\x0frecommendations\x18\x02 \x03(\x0b\x32\x1b.recommender.Recommendation"^\n\x1aGroupRecommendationRequest\x12\x10\n\x08\x61nimeIds\x18\x01 \x03(\x05\x12\x0e\n\x01k\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x10\x65xcludedAnimeIds\x18\x03 \x03(\x05\x42\x04\n\x02_k"S\n\x1bGroupRecommendationResponse\x12\x34\n\x0frecommendations\x18\x01 \x03(\x0b\x32\x1b.recommender.Recommendation2\x9b\x02\n\x0bRecommender\x12?\n\tIsTrained\x12\x12.recommender.Empty\x1a\x1e.recommender.IsTrainedResponse\x12]\n\x12GetRecommendations\x12".recommender.RecommendationRequest\x1a#.recommender.RecommendationResponse\x12l\n\x17GetGroupRecommendations\x12\'.recommender.GroupRecommendationRequest\x1a(.recommender.GroupRecommendationResponseb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "recommender_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _RECOMMENDATION._serialized_start = 34
    _RECOMMENDATION._serialized_end = 92
    _EMPTY._serialized_start = 94
    _EMPTY._serialized_end = 101
    _ISTRAINEDRESPONSE._serialized_start = 103
    _ISTRAINEDRESPONSE._serialized_end = 139
    _RECOMMENDATIONREQUEST._serialized_start = 141
    _RECOMMENDATIONREQUEST._serialized_end = 229
    _RECOMMENDATIONRESPONSE._serialized_start = 231
    _RECOMMENDATIONRESPONSE._serialized_end = 326
    _GROUPRECOMMENDATIONREQUEST._serialized_start = 328
    _GROUPRECOMMENDATIONREQUEST._serialized_end = 422
    _GROUPRECOMMENDATIONRESPONSE._serialized_start = 424
    _GROUPRECOMMENDATIONRESPONSE._serialized_end = 507
    _RECOMMENDER._serialized_start = 510
    _RECOMMENDER._serialized_end = 793
# @@protoc_insertion_point(module_scope)