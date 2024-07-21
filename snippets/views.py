from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Snippet, Tag
from rest_framework.permissions import AllowAny
from .serializers import SnippetSerializer, TagSerializer, UserSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class SnippetListCreateView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

class TagDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        snippets = Snippet.objects.filter(tag=tag, user=request.user)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

class SnippetOverview(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_snippets = Snippet.objects.filter(user=request.user).count()
        snippets = Snippet.objects.filter(user=request.user)
        serializer = SnippetSerializer(snippets, many=True)
        return Response({
            'total_count': total_snippets,
            'snippets': serializer.data
        })
