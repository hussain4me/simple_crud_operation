from rest_framework import serializers
from .models import User_Profile, User

class UserProfileSerilier(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = ['name','sex','user','track', 'created']

 