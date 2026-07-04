from rest_framework.views import APIView
from rest_framework.response import Response


class ChatAPIView(APIView):

    def post(self,request):

        query=request.data.get("query")

        return Response({

            "query":query,

            "response":"Ollama integration in Phase 5."

        })