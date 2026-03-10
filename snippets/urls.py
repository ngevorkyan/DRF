# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

from django.urls import path
from snippets import views  # your app

urlpatterns = [
    path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
    path("users/", views.UserList.as_view(), name="user-list"),

    path("api/", views.api_root),  # DRF API root
    path("", views.home),           # your frontend homepage
]      # frontend homepage




