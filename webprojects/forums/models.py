from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title=models.CharField(max_length=64)
    content=models.TextField()
    date= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}|"
