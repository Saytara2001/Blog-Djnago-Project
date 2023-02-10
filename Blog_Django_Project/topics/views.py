from django.shortcuts import render
from rest_framework import viewsets

from topics.models import Topic
from topics.serializers import TopicSerializer


# Create your views here.


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
