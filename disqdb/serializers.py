from rest_framework import serializers
from .models import Pitch

class readingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pitch
        fields = ['timestamp', 'value']