from rest_framework import serializers
from .models import Pitch, TestRecord

class readingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pitch
        fields = ['timestamp', 'value']

class TestRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestRecord
        fields = ['name', 'start_time', 'end_time']