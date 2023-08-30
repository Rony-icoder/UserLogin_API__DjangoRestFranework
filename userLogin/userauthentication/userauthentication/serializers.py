from rest_framework import serializers
from django.contrib.auth.models import User
from db.models import Empolyee

class EmpolyeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empolyee
        fields = []


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    
    def create(self,data):
        user = User.objects.create(username = data["username"])
        user.set_password(data["password"])
        user.save()
        return data

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()