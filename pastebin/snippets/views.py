from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
  """
  List all snippets, or create a new snippet.
  """
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  Retrieve, update or delete a snippet instance
  """
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
