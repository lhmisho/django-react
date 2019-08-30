from django.urls import path

from .views import ArticleListApi, ArticleDetailApi

urlpatterns = [

    path('', ArticleListApi.as_view()),
    path('<pk>', ArticleDetailApi.as_view()),
]
