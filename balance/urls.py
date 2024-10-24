from django.urls import path
from .views import UserBalanceView, TransferView, AllUsersView, UserCreateView

urlpatterns = [
    path('api/create-user/', UserCreateView.as_view(), name='create-user'),
    path('balance/<int:user_id>/', UserBalanceView.as_view(), name='user-balance'),
    path('balance/all/', AllUsersView.as_view(), name='all-users'),  # Получение списка всех пользователей
    path('transfer/', TransferView.as_view(), name='transfer'),  # Перевод средств
]
