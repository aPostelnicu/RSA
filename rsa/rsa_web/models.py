from django.db import models

class Message(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title