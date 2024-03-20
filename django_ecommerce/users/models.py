from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from main.models import Badge

# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    # password field defined in base class
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rank = models.CharField(max_length=50, default="Padwan")
    badges = models.ManyToManyField(Badge)
    bigCoID = models.CharField(max_length=50, unique=True)

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

        # set bigCoID
        new_user.bigCoID = ("%s%s%s" % (
            new_user.name[:2], new_user.rank[:1],
            datetime.now().strftime("%Y%m%d%H%M%S%f"),
            )
        )
        new_user.save()
        return new_user

    def __str__(self) -> str:
        return self.email