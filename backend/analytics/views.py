from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response

from sales.models import Sale


class DashboardAPIView(APIView):

    def get(self,request):

        revenue=Sale.objects.aggregate(
            total=Sum("unit_price")
        )

        return Response(revenue)