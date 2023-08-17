from django.urls import path
from .views import *
urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    # usint mixin
    path('SnippetList/', SnippetList.as_view()),
    path('SnippetList/<int:pk>/', SnippetDetail.as_view()),
    # generic
    path('SnippetGenericList/', SnippetGenericList.as_view()),
    path('SnippetGenericList/<int:pk>/', SnippetGenericDetail.as_view()),
]