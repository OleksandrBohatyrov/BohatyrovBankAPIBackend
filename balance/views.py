from rest_framework import status
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserBalance
from .serializers import UserBalanceSerializer, UserCreateSerializer, BalanceUpdateSerializer
from drf_yasg.utils import swagger_auto_schema

class UserBalanceView(APIView):
    """
    API для работы с балансом пользователя.
    """
    def get(self, request, user_id):
        try:
            user_balance = UserBalance.objects.get(user_id=user_id)
            serializer = UserBalanceSerializer(user_balance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserBalance.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Описание параметра amount
    amount_param = openapi.Parameter(
        'balance', in_=openapi.IN_BODY, description='Сумма для начисления на баланс', type=openapi.TYPE_NUMBER
    )

    @swagger_auto_schema(request_body=BalanceUpdateSerializer)
    def post(self, request, user_id):
        """
        Начисление средств на баланс пользователя.
        """
        serializer = BalanceUpdateSerializer(data=request.data)
        if serializer.is_valid():
            balance = serializer.validated_data['balance']
            try:
                user_balance, created = UserBalance.objects.get_or_create(user_id=user_id)
                user_balance.balance += balance
                user_balance.save()
                return Response({"message": "Balance updated successfully"}, status=status.HTTP_200_OK)
            except UserBalance.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, *args, **kwargs):
        try:
            user_balance = UserBalance.objects.get(user_id=user_id)
        except UserBalance.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserBalanceSerializer(user_balance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransferView(APIView):
    """
    API для перевода средств между пользователями.
    """
    def post(self, request):
        from_user_id = request.data.get('from_user_id')
        to_user_id = request.data.get('to_user_id')
        amount = request.data.get('amount')

        if not from_user_id or not to_user_id or not amount:
            return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            from_user = UserBalance.objects.get(user_id=from_user_id)
            to_user, created = UserBalance.objects.get_or_create(user_id=to_user_id)

            if from_user.balance >= float(amount):
                from_user.balance -= float(amount)
                to_user.balance += float(amount)
                from_user.save()
                to_user.save()
                return Response({"success": "Transfer completed"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
        except UserBalance.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class UserCreateView(APIView):
    """
    API для создания новых пользователей.
    """
    
    @swagger_auto_schema(request_body=UserCreateSerializer)  # добавляем сериализатор для отображения полей в Swagger
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllUsersView(APIView):
    """
    API для получения списка всех пользователей и их баланса.
    """
    def get(self, request):
        user_balances = UserBalance.objects.all()
        serializer = UserBalanceSerializer(user_balances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
