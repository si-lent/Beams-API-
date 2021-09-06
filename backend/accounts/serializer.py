from rest_framework import serializers
from .models import User_Profile

class User_Profile_Serializer (serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source = 'user.email')

    class Meta:
        model = User_Profile
        fields = ['user', 'University', 'First_Name', 'Last_Name', 'Date_Made', 'Date_Modified']