from users.models import User, Region
from rest_framework import serializers

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('region', 'region_name')

class UserSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('num', 'first_name', 'last_name', 'gender', 'age', 'region')