from .models import News
from.serializers import NewsSerializer
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class NewsViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
    permission_classes=[AllowAny]

