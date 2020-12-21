from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']