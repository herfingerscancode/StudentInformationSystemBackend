from rest_framework import serializers

from mainApp.models import Result, Student


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ()


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ()

