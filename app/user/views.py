from rest_framework import generics

from user.serializers import UserSerialzer


class CreateUserView(generics.CreateAPIView):
    """Create a new user is the system"""
    serializer_class = UserSerialzer
