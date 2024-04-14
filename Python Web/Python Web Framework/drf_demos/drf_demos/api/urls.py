from django.urls import path
from rest_framework.routers import DefaultRouter

from drf_demos.api.views import AuthorsApiView, AuthorsView, AuthorsApiViewSet

router = DefaultRouter()

router.register('authors-vs', AuthorsApiViewSet, basename='author')

urlpatterns = (
    path('authors/', AuthorsApiView.as_view(), name='api list authors'),
    path('authors-ssr/', AuthorsView.as_view(), name='list authors'),
    path('authors-vs/', AuthorsApiViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }))
)
