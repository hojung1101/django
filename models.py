
from django.db import models
from django.utils import timezone
# Create your models here.
class Board(models.Model):

    id = models.AutoField(primary_key = True)

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

class Comment(models.Model):
    board = models.ForeignKey("Board",
                              models.SET_NULL,
                              blank=True,
                              null=True,
                              )


    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)