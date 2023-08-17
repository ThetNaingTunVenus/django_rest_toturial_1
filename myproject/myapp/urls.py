from django.urls import path
from .views import *
urlpatterns = [
    path('article_list/', article_list),
    path('article_detail/<int:pk>/', article_detail),

    path('student_api/', student_api),
    path('student_data/',student_data),
    path('snippet_detail/<int:pk>/', snippet_detail),
    path('snippet_list/', snippet_list),
]