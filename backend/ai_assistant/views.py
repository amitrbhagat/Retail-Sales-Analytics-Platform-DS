from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ChatSerializer
from .services import ask_llm


class ChatView(APIView):

    def post(self,request):

        serializer = ChatSerializer(
            data = request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        answer = ask_llm(
            serializer.validated_data["question"]
        )

        return Response({
            "answer":answer
        })