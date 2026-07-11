from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    ask_llm,
    get_forecast,
    get_inventory,
    get_analytics,
)

from .serializers import ChatSerializer


class ChatView(APIView):

    def post(self, request):

        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        answer = ask_llm(
            serializer.validated_data["question"]
        )

        return Response({
            "answer": answer
        })


class ForecastView(APIView):

    def post(self, request):

        return Response(get_forecast())


class InventoryView(APIView):

    def post(self, request):

        return Response(get_inventory())


class AnalyticsView(APIView):

    def post(self, request):

        return Response(get_analytics())