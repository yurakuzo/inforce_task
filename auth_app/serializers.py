from rest_framework import serializers
from .models import Vote, Employee
from django.contrib.auth.password_validation import validate_password


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Employee
        fields = ['full_name', 'password']

    def create(self, validated_data):
        user = Employee.objects.create(full_name=validated_data['full_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

