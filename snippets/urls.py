from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('snippets/', SnippetListCreate.as_view()),
    path('snippets/<int:pk>/', SnippetDetailUpdateDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)