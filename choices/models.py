from django.db import models
# import UserModel from django.contrib.auth.models
from accounts.models import CustomUser


class Choice(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.choice_text
