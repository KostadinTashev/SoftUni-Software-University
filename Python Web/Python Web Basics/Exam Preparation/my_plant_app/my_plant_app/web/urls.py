from django.urls import path, include

from my_plant_app.web.views import index, catalogue, \
    create_profile, details_profile, edit_profile, delete_profile, \
    create_plant, details_plant, edit_plant, delete_plant

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>/', details_plant, name='details plant'),
    path('edit/<int:pk>/', edit_plant, name='edit plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
