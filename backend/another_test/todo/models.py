from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(default='', blank=True)

    created_by = models.ForeignKey(USER, on_delete=models.DO_NOTHING)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title