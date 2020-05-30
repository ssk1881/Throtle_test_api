from django.db import models


class User(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    real_name = models.CharField(max_length=250)
    tz = models.CharField(max_length=250)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    pid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_periods')
    start_time = models.CharField(max_length=260)
    end_time = models.CharField(max_length=250)
