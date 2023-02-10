from django.db import models
from django.utils.text import Truncator
from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    short_message = serializers.SerializerMethodField("get_short_message")

    def get_short_message(self, Post):
        return Truncator(Post.message).chars(10)

    class Meta:
        model = Post
        fields = '__all__'
