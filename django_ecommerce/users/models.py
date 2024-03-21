from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from main.models import Badge

# Create your models here.
class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    # password field defined in base class
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rank = models.CharField(max_length=50, default="Padwan")
    badges = models.ManyToManyField(Badge)
    bigCoID = models.CharField(max_length=50, unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

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

    def has_module_perms(self, app_label):
        # Kullanıcının belirli bir uygulama modülüne erişip erişemeyeceğini belirle
        # Bu örnekte her kullanıcıya her uygulama modülüne erişim izni veriyoruz.
        return True

    def has_perm(self, perm, obj=None):
        # Kullanıcının belirli bir izne sahip olup olmadığını belirle
        # Bu örnekte her kullanıcıya her izin veriliyor.
        return True