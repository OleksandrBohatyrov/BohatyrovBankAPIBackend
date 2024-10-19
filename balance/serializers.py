from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserBalance

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},  # Чтобы пароль не отображался в ответах
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class UserBalanceSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)  # Добавляем поле username из модели User

    class Meta:
        model = UserBalance
        fields = ['user_id', 'username', 'balance']  # Теперь username корректно связано

class BalanceUpdateSerializer(serializers.Serializer):
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)