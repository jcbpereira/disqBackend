# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import Pitch, TestRecord
from .posture_buffer import add_pitch_measurement, get_current_average

@api_view(['GET', 'POST'])
def add_pitch_reading(request):
    # Request format {'tmestamp': datetime, 'value': float}
    if request.method == 'POST':
        serializer = readingSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            # Add to rolling average buffer
            avg=add_pitch_measurement(instance.value)
            # Also return rolling average in the response
            return Response({"average": round(avg, 0)},status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        data = Pitch.objects.all()

        serializer = readingSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

@api_view(['GET', 'POST'])
def record_test_run(request):

    if request.method == 'POST':
        serializer = TestRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        data = TestRecord.objects.all()

        serializer = TestRecordSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)