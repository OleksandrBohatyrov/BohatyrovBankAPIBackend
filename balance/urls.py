from django.urls import path
from .views import UserBalanceView, TransferView

urlpatterns = [
    path('balance/<int:user_id>/', UserBalanceView.as_view()),  # Получение баланса пользователя
    path('balance/', UserBalanceView.as_view()),  # Начисление и списание средств
    path('transfer/', TransferView.as_view()),  # Перевод средств между пользователями
]
