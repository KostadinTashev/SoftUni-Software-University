from django.urls import path

from user_password_demos.app_auth.views import RegisterUserView, LoginUserView, LogoutUserView, UsersListView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('', UsersListView.as_view(), name='users list'),

)

# t@sh3v$!
