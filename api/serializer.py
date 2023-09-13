from rest_framework import serializers
from .models import Person

class UserProfileSerilier(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name','sex','track', 'created']

