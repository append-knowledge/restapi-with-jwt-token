from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from project.models import MyUser


class Signupserializer(ModelSerializer):
    class Meta:
        model=MyUser
        fields=['username','email','password','address']

        def create(self,validated_data):
            return MyUser.objects.create_user(username=validated_data['username'],password=validated_data['password'],
                                              email=validated_data['email'],address=validated_data['address'])


class SignInserializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()

class UserDetailsserializer(ModelSerializer):
    class Meta:
        model=MyUser
        fields=['username','email','address']
