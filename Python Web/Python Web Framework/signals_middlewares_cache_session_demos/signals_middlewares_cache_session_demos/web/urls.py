from django.urls import path

from signals_middlewares_cache_session_demos.web.views import index, create_task, details_task
from .signals import *

urlpatterns = (
    path('', index, name='index'),
    path('create/', create_task, name='create task'),
    path('details_task/<int:pk>/', details_task, name='details task'),
)
