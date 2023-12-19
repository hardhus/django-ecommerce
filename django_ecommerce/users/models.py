from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    # password field defined in base class
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    @classmethod
    def get_by_id(cls, uid):
        return User.objects.get(pk=uid)
    
    @classmethod
    def create(cls, name, email, password):
        new_user = cls(
            name=name,
            email=email,
        )
        new_user.set_password(password)
        new_user.save()
        return new_user

    def __str__(self) -> str:
        return self.email