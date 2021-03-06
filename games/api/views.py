from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer

from games.api.serializers import (PlatformSerializer, 
                                   DeveloperSerializer, 
                                   GenreSerializer, 
                                   PublisherSerializer, 
                                   GameSerializer)
from games.models import Platform, Developer, Genre, Publisher, Game


class PlatformListAPIView(generics.ListAPIView):
    """Provide a read-only view for platforms"""
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class DeveloperListAPIView(generics.ListAPIView):
    """Provide a read-only view for developers"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class DeveloperDetailAPIView(APIView):

    def get_object(self, pk):
        developer = get_object_or_404(Developer, pk=pk)
        return developer

    def get(self, request, pk):
        developer = self.get_object(pk)
        serializer = DeveloperSerializer(developer)
        return Response(serializer.data)


class GenreListAPIView(generics.ListAPIView):
    """Provide a read-only view for genres"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PublisherListAPIView(generics.ListAPIView):
    """Provide a read-only view for publishers"""
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class GameListAPIView(generics.ListAPIView):
    """Provide a read-only view for games"""
    # renderer_classes = [JSONRenderer]
    queryset = Game.objects.all().order_by('-created_at')
    serializer_class = GameSerializer


