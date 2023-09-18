from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Prediction(models.Model):
    user = models.ForeignKey(User, related_name='predictions', on_delete=models.CASCADE)
    team1 = models.CharField(max_length=100, null=True)
    team2 = models.CharField(max_length=100, null=True)
    #left parameters
    rdLeft = models.IntegerField(default = 0)
    eraLeft = models.IntegerField(default = 0)
    fipLeft = models.IntegerField(default = 0)
    lobLeft = models.IntegerField(default = 0)
    whipLeft = models.IntegerField(default = 0)
    obpLeft = models.IntegerField(default = 0)
    slgLeft = models.IntegerField(default = 0)
    percentageLeft = models.IntegerField(default = 0)
    baLeft = models.IntegerField(default = 0)

    #Right Parameters
    rdRight = models.IntegerField(default = 0)
    eraRight = models.IntegerField(default = 0)
    fipRight = models.IntegerField(default = 0)
    lobRight = models.IntegerField(default = 0)
    whipRight = models.IntegerField(default = 0)
    obpRight = models.IntegerField(default = 0)
    slgRight = models.IntegerField(default = 0)
    baRight = models.IntegerField(default = 0)
    percentageRight = models.IntegerField(default = 0)
    percentage = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.team1} vs {self.team2} by {self.user.username}"
