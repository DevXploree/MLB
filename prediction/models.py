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
        return f"Prediction for {self.team1} vs {self.team2} by {self.user.username}"\
    

class Stats(models.Model):
    team_name = models.CharField(max_length=300, blank=True, null=True)
    batters_used = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    batting_age = models.CharField(blank=True, null=True, max_length=300)
    runs_per_game = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    game_played = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    plate_appearances = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    at_bats = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    run_scored = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    hits = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    doubles = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    triples = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    home_runs = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    rbis = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    stolen_bases = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    caught_stealing = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    bases_on_balls = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    strikeouts = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    batting_avg = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    onbase_perc = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    slugging_perc = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    ops = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    ops_plus = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    total_bases = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    double_plays = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    hit_by_pitch = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    sac_hits = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    sac_flies = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    intentional_bb = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    left_on_base = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    floatentional_bb = models.DecimalField(blank=True, null=True, decimal_places=4, max_digits=13)
    
    def __str__(self):
        return f"{self.team_name} - Stats"
    

