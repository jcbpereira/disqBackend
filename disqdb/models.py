from django.db import models

# Every time I make I change here I need to run python manage.py makemigrations
# and python manage.py migrate
# Create your models here.
class Pitch(models.Model):
    timestamp = models.DateTimeField()
    value = models.FloatField()

# Create a new model that stores start and end time of test runs with name
# Then I can just filter out the test runs that I want to see manually
# No need to create relationships between the two models
class TestRecord(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()