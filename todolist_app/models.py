from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.task} - {'' if self.done else 'Not '}Completed"
