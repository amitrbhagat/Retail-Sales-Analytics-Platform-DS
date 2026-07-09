from rest_framework import serializers


class RecommendationSerializer(serializers.Serializer):

    product = serializers.CharField()

    current_stock = serializers.IntegerField()

    forecast = serializers.FloatField()

    recommendation = serializers.CharField()