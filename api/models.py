from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        OPS = 'OPS', _('Ops User')
        CLIENT = 'CLIENT', _('Client User')

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.CLIENT)
    is_verified = models.BooleanField(default=False)

class File(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)