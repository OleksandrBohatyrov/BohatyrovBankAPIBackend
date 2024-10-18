from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserBalance
from .serializers import UserBalanceSerializer

class UserBalanceView(APIView):

    def get(self, request, user_id):
        """
        Получение текущего баланса пользователя.
        """
        try:
            user_balance = UserBalance.objects.get(user_id=user_id)
            serializer = UserBalanceSerializer(user_balance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserBalance.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        Начисление средств на баланс пользователя.
        """
        user_id = request.data.get('user_id')
        amount = request.data.get('amount')
        if not user_id or not amount:
            return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        user_balance, created = UserBalance.objects.get_or_create(user_id=user_id)
        user_balance.balance += float(amount)
        user_balance.save()

        return Response(UserBalanceSerializer(user_balance).data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        Списание средств с баланса пользователя.
        """
        user_id = request.data.get('user_id')
        amount = request.data.get('amount')
        if not user_id or not amount:
            return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_balance = UserBalance.objects.get(user_id=user_id)
            if user_balance.balance >= float(amount):
                user_balance.balance -= float(amount)
                user_balance.save()
                return Response(UserBalanceSerializer(user_balance).data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
        except UserBalance.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class TransferView(APIView):
    def post(self, request):
        """
        Перевод средств от одного пользователя другому.
        """
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
