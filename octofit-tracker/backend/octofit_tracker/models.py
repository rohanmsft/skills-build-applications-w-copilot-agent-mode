from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)

class User(AbstractUser):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    email = models.EmailField(unique=True)

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    distance = models.FloatField()

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    reps = models.IntegerField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
