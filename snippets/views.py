# snippets/views.py
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer, UserSeiralizer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
class UserList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSeiralizer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSeiralizer
    