from django.contrib import admin
from .models import UserBalance 

@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')  # Показываем юзера и баланс
    search_fields = ('user__username',)  # Возможность искать по имени юзера
    list_editable = ('balance',)  # Разрешаем редактировать баланс напрямую в списке
