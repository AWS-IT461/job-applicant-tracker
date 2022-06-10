from rest_framework import serializers

from backend.trackerr import models


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class CompanyDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.CompanyDetail
        fields = "__all__"


class CompanyModelSerializer(serializers.ModelSerializer):
    detail = CompanyDetailModelSerializer(many=True, read_only=True)

    class Meta:
        model = models.Company
        fields = "__all__"


class JobApplicationModelSerializer(serializers.ModelSerializer):
    company = CompanyModelSerializer(read_only=True)

    class Meta:
        model = models.JobApplication
        fields = "__all__"


class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = "__all__"
