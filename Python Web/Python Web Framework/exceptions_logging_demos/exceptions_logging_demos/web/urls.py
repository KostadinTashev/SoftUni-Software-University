from django.urls import path

from exceptions_logging_demos.web.views import index

urlpatterns = (
    path('', index, name='index'),
)