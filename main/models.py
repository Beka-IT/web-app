from django.db import models

class Films(models.Model):
    name = models.CharField(max_length=40)
    premiere_year = models.IntegerField()
    country = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    duration = models.IntegerField()
    producer = models.CharField(max_length=40)
    cast = models.CharField(max_length=150)
    picture_url = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255)
    isSolo = models.BooleanField(default=True)


class FutureFilms(models.Model):
    name = models.CharField(max_length=40)
    picture_url = models.CharField(max_length=255)
