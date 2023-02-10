from django.db import models
from model_utils.models import TimeStampedModel


class Board(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
