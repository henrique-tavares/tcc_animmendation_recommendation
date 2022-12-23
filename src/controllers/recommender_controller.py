from loguru import logger

from infra.grpc.recommender_pb2 import (
    Empty,
    GroupRecommendationRequest,
    GroupRecommendationResponse,
    IsTrainedResponse,
    Recommendation,
    RecommendationRequest,
    RecommendationResponse,
)
from infra.grpc.recommender_pb2_grpc import RecommenderServicer
from services.recommender_service import RecommenderService
from utils.method_logger import MethodLogger


class RecommenderController(RecommenderServicer):
    def IsTrained(self, request: Empty, context):
        with logger.catch(), MethodLogger("IsTrained"):
            trained = RecommenderService.check_is_trained()
            return IsTrainedResponse(trained=trained)

    def GetGroupRecommendations(self, request: GroupRecommendationRequest, context):
        with logger.catch(), MethodLogger("GetGroupRecommendations"):

            animes_rec = RecommenderService.group_nearest_neighbors(
                list(request.animeIds), list(request.excludedAnimeIds), request.amount, request.offset
            )
            return GroupRecommendationResponse(
                recommendations=[
                    Recommendation(recommendedAnimeId=anime_id, rank=i + 1)
                    for i, (anime_id, distance) in enumerate(animes_rec)
                ]
            )

    def GetRecommendations(self, request: RecommendationRequest, context):
        with logger.catch(), MethodLogger("GetRecommendations"):

            recommendations = RecommenderService.nearest_neighbors(
                request.animeId, request.amount, request.offset, list(request.excludedAnimeIds)
            )
            return RecommendationResponse(
                animeId=request.animeId,
                recommendations=[
                    Recommendation(recommendedAnimeId=anime_id, rank=i + 1)
                    for i, (anime_id, distance) in enumerate(recommendations)
                ],
            )
