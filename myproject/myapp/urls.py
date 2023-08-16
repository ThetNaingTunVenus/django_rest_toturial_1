from django.urls import path
from .views import *
urlpatterns = [
    path('article_list/', article_list),
    path('article_detail/<int:pk>/', article_detail),
]