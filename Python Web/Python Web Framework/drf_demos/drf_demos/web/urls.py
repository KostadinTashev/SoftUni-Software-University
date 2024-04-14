from django.urls import path
from rest_framework.routers import DefaultRouter

from drf_demos.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
