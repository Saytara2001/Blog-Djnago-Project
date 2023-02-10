from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel
from boards.models import Board


class Topic(TimeStampedModel):
    subject = models.CharField(max_length=50)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='topics', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.subject
