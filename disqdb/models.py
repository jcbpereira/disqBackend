from django.db import models

# Every time I make I change here I need to run python manage.py makemigrations
# and python manage.py migrate
# Create your models here.
class Pitch(models.Model):
    timestamp = models.DateTimeField()
    value = models.FloatField()