from pkg_resources import require
from rest_framework import serializers


class JobApplicationQuerySerializer(serializers.Serializer):
    user = serializers.CharField(required=False)


class EventQuerySerializer(serializers.Serializer):
    user = serializers.CharField(required=False)
    application = serializers.CharField(required=False)


class CompanyQuerySerializer(serializers.Serializer):
    user = serializers.CharField(required=False)
