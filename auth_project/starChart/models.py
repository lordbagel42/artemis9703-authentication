from django.db import models
from django.contrib.auth.models import User

class starSighting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star_name = models.CharField(max_length=100)
    date_seen = models.DateField()

    def __str__(self):
        return f"{self.star_name} seen on {self.date_seen}"