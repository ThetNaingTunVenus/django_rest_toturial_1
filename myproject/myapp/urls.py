from django.urls import path
from .views import *
urlpatterns = [
    path('article_list/', article_list),
    # path('myapp/<int:pk>/', views.snippet_detail),
]