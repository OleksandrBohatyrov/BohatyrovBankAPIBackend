from rest_framework import serializers
from .models import UserBalance

class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBalance
        fields = ['user_id', 'balance']
