from django.contrib.auth.models import User
from django.db import models
import random

def generate_code():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

class VerificationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verification_code')
    code = models.CharField(max_length=6, default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Code for {self.user.username}: {self.code}'