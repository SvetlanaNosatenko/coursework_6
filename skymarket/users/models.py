from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager
from django.db import models


class UserRoles:
    USER = "user"
    ADMIN = "admin"


class User(AbstractBaseUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    ROLES = [
        ("user", "Пользователь"),
        ("admin", "Админ"),
    ]

    first_name = models.CharField(max_length=64, verbose_name="Имя",
                                  help_text="Введите имя, макс 64 символа")
    last_name = models.CharField(max_length=64, verbose_name="Фамилия",
                                 help_text="Введите фамилию, макс 64 символа")
    phone = models.CharField(max_length=15, verbose_name="Укажите телефон для связи",
                             help_text="Укажите телефон для связи")
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email address",
                              help_text="Укажите электронную почту")
    role = models.CharField(max_length=9, choices=ROLES, default="user", verbose_name="Роль пользователя",
                            help_text="Укажите роль пользователя")
    is_active = models.BooleanField(default=False, null=True, verbose_name="Аккаунт активен",
                                    help_text="Укажите активен ли аккаунт")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def save(self, *args, **kwargs):
        self.set_password(self.password)

        super().save()

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
