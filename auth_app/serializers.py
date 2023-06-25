from rest_framework import serializers
from .models import Vote, Employee
from django.contrib.auth.password_validation import validate_password


class VoteSerializer(serializers.ModelSerializer):
    """Basic Vote Serializer"""

    class Meta:
        model = Vote
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """Basic Employee Serializer"""
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'votes']  # Fixed JSON response here

    def get_votes(self, obj):
        votes = Vote.objects.filter(user=obj)
        return VoteSerializer(votes, many=True).data


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    """Employee Registration Serializer"""

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'password']

    def create(self, validated_data):
        user = Employee.objects.create(full_name=validated_data['full_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
