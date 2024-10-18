from django.contrib import admin
from .models import UserBalance 

@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')  
    search_fields = ('user__username',) 
    list_editable = ('balance',)  



