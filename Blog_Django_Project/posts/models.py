from django.contrib.auth.models import User
from django.db import models
from django.utils.text import Truncator
from model_utils.models import TimeStampedModel
from topics.models import Topic


class Post(TimeStampedModel):
    message = models.CharField(max_length=5000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return Truncator(self.message).chars(10)
