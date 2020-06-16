from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    body = models.TextField(default='')
    date = models.DateField()

    def __str__(self):
        return self.title