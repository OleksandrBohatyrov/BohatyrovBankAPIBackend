from django.contrib.auth.models import User
from django.db import models

class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с моделью User
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.balance} руб."
