from rest_framework import serializers
from bson import ObjectId

# Helper to convert ObjectId to string
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

# User Serializer
class UserSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    # Add more fields as needed

# Team Serializer
class TeamSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=ObjectIdField())

# Activity Serializer
class ActivitySerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    user = ObjectIdField()
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    timestamp = serializers.DateTimeField()

# Leaderboard Serializer
class LeaderboardSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    user = ObjectIdField()
    score = serializers.IntegerField()

# Workout Serializer
class WorkoutSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    user = ObjectIdField()
    name = serializers.CharField(max_length=100)
    exercises = serializers.ListField(child=serializers.CharField(max_length=100))
