from rest_framework import serializers
from boards.models import Board


# HyperlinkedModelSerializer : this put url to (Delete, Update) item
class BoardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'
