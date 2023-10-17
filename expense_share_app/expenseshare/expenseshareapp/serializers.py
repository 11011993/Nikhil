from rest_framework import serializers
from expenseshareapp.models import Calculateexpense
from django.contrib.auth.models import User

class AmountandparticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculateexpense
        fields = "__all__"

class UserregisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'email', 'password','username')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"