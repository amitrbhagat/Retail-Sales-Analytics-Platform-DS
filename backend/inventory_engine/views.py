from rest_framework.views import APIView
from rest_framework.response import Response

from .services import generate_recommendations


class RecommendationView(APIView):

    def get(self, request):

        recommendations = generate_recommendations()

        return Response(recommendations)