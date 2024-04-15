from django.urls import path, include

from fruitipedia_app.web.views import index, dashboard, \
    add_fruit, details_fruit, edit_fruit, delete_fruit, \
    add_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', add_profile, name='add profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),
    path('fruit/create/', add_fruit, name='add fruit'),
    path('fruit/<int:pk>/', include([
        path('details/', details_fruit, name='details fruit'),
        path('edit/', edit_fruit, name='edit fruit'),
        path('delete/', delete_fruit, name='delete fruit'),
    ])),
)
