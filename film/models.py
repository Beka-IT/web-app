from django.db import models
from main.models import Films
from django.contrib.auth.models import User
class Comments(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.ForeignKey(Films,on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
