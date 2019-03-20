from rest_framework import serializers

class Followers(serializers.Serializer):
    username = serializers.CharField(required=True)
