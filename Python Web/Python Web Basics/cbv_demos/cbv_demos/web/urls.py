from django.urls import path

from cbv_demos.web.views import list_articles, ArticlesListView, RedirectToArticlesView, ArticleDetailView, \
    ArticleCreateView, ArticleDeleteView

urlpatterns = (
    path('', list_articles, name='list articles'),
    path('cbv/', ArticlesListView.as_view(), name='list articles cbv'),
    # path('cbv/<int:id>/', ArticlesListView.as_view(), name='list articles cbv by'),
    path('redirect-to-articles/', RedirectToArticlesView.as_view(), name='redirect articles'),
    path('cbv/<int:pk>/', ArticleDetailView.as_view(), name='details article'),
    path('cbv/create/', ArticleCreateView.as_view(), name='create article'),
    path('cbv/delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete article'),
)
