from django.urls import path, include

from eventer_app.web.views import index, dashboard, \
    add_event, details_event, edit_event, delete_event, \
    add_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', add_profile, name='add profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('create/', add_event, name='add event'),
    path('details/<int:pk>/', details_event, name='details event'),
    path('edit/<int:pk>/', edit_event, name='edit event'),
    path('delete/<int:pk>/', delete_event, name='delete event'),
)
