from django.contrib.auth.models import User
from rest_framework import serializers


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_active', 'is_superuser')
        read_only_fields = ('id', 'is_active', 'is_superuser')
