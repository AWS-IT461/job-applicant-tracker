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

    def checkEmailExists(self, email):
        return models.User.objects.filter(email=email).exists()

    @action(methods=["POST"], detail=False)
    def signup(self, request):
        serializer = serializers.request.SignupRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if self.checkEmailExists(email := serializer.validated_data["email"]):
            return Response("Email already taken", status=status.HTTP_400_BAD_REQUEST)

        password = serializer.validated_data["password"]

        user = models.User.objects.create_user(email=email, password=password)

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

    def get_queryset(self):
        serializer = serializers.query.JobApplicationQuerySerializer(
            data=self.request.query_params
        )

        queryset = self.queryset

        if not serializer.is_valid(raise_exception=True):
            return queryset.all()

        if user := serializer.validated_data.get("user"):
            queryset = queryset.filter(user=user)

        return queryset.all()


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

    def get_queryset(self):
        serializer = serializers.query.JobApplicationQuerySerializer(
            data=self.request.query_params
        )

        queryset = self.queryset

        if not serializer.is_valid(raise_exception=True):
            return queryset.all()

        if user := serializer.validated_data.get("user"):
            queryset = queryset.filter(user=user)

        return queryset.all()

    @action(methods=["GET"], detail=True)
    def count(self, request, pk):
        return Response(
            {
                "accepted": models.JobApplication.objects.filter(
                    user=pk, status="A"
                ).count(),
                "pending": models.JobApplication.objects.filter(
                    user=pk, status="P"
                ).count(),
                "rejected": models.JobApplication.objects.filter(
                    user=pk, status="R"
                ).count(),
            }
        )


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

    def get_queryset(self):
        serializer = serializers.query.CompanyQuerySerializer(
            data=self.request.query_params
        )

        queryset = self.queryset

        if not serializer.is_valid(raise_exception=True):
            return queryset.all()

        if user := serializer.validated_data.get("user"):
            queryset = queryset.filter(companydetail__user=user)

        return queryset.all()
