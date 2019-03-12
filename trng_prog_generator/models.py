from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Athlete (models.Model):
    name = models.CharField(max_length=100,null=True, unique=True)
    is_still_trng = models.BooleanField(default=True)
    body_weight= models.FloatField(default=10)
    snatch_pr = models.FloatField(default=10)
    cj_pr = models.FloatField(default=10)

    def __str__ (self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)
    athlete = models.ForeignKey(Athlete, related_name='Athlete', on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Programme(models.Model):
    training_mode = models.TextField(max_length = 150, null=True)
    view_by_athlete = models.ForeignKey(Athlete, related_name='athlete_view', on_delete=models.CASCADE)
    created_by_coach = models.ForeignKey(Coach,related_name='coach_create', on_delete=models.CASCADE)
    updated_by_coach = models.ForeignKey(Coach,related_name='coach_update', on_delete=models.CASCADE)






