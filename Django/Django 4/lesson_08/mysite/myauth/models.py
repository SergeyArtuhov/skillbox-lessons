from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )  # связываем новую модель с моделью User и указываем что при удалении юзера удаляется и профиль
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)