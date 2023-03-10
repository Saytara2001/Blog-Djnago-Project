from django.shortcuts import render
from rest_framework import viewsets

from boards.models import Board
from boards.serializers import BoardSerializer


# Create your views here.


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
