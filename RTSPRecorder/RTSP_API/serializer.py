from rest_framework import serializers
from .models import Recording,Camera

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('name','url','status','active_hours')

class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = ('name','path','status','recorded_time')