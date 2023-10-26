from django.db import models
from django.conf import settings

# Create your models here.
class URL(models.Model):
    title = models.TextField()
    long_url = models.TextField()
    short_url = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title