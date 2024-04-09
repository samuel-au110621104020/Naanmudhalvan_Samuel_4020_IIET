from django.db import models

class Song(models.Model):
    title=models.TextField()
    artist=models.TextField()
    image=models.ImageField()
    audio_file=models.FileField()
    audio_link=models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)

class watchlater(models.Model):
    title=models.TextField()
    artist=models.TextField()
    image=models.ImageField()
    audio_file=models.FileField()
    audio_link=models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)

class history(models.Model):
    title=models.TextField()
    artist=models.TextField()
    image=models.ImageField()
    audio_file=models.FileField()
    audio_link=models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)