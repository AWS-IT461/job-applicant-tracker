from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import mixins, status, viewsets, serializers as serializer
from rest_framework.decorators import action
from backend.trackerr import serializers, models
from backend.trackerr import pagination


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = serializers.base.UserModelSerializer
    queryset = models.User.objects

    @action(methods=["POST"], detail=False)
    def login(self, request):
        serializer = serializers.request.LoginRequestSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        login(request, user)

        return Response(self.get_serializer(user).data)


class EventViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = serializers.base.EventModelSerializer
    queryset = models.Event.objects


class JobApplicationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.base.JobApplicationModelSerializer
    queryset = models.JobApplication.objects.all()
    pagination_class = pagination.StandardResultsSetPagination


class CompanyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.base.CompanyModelSerializer
    queryset = models.Company.objects
