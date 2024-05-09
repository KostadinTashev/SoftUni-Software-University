from django.urls import path, include

from tasty_recipes_app.web.views import home_page, catalogue, \
    create_profile, details_profile, edit_profile, delete_profile, \
    create_recipe, details_recipe, edit_recipe, delete_recipe

urlpatterns = (
    path('', home_page, name='home page'),
    path('recipe/', include([
        path('catalogue/', catalogue, name='catalogue'),
        path('create/', create_recipe, name='create recipe'),
        path('<int:recipe_id>/details/', details_recipe, name='details recipe'),
        path('<int:recipe_id>/edit/', edit_recipe, name='edit recipe'),
        path('<int:recipe_id>/delete/', delete_recipe, name='delete recipe'),
    ])),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
)
