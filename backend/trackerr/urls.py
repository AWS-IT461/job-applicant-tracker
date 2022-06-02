from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.trackerr import views


ROUTER = DefaultRouter()

ROUTER.register("users", views.UserViewSet)
ROUTER.register("applications", views.JobApplicationViewSet)
ROUTER.register("events", views.EventViewSet)
ROUTER.register("companies", views.CompanyViewSet)


urlpatterns = path("", include(ROUTER.urls))
