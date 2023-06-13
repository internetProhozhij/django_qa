# https://docs.djangoproject.com/en/4.2/topics/db/models/

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Не хочу использовать стандартную таблицу пользователей потому,
# что там много ненужных полей. Мне достаточно только:
#     - username: имя пользователя (PK)
#     - password: пароль;
#     - is_god: админ или не админ.
class AccountManager(BaseUserManager):
    """
    Магическая штука, которая управляет созданием записей
    в таблице пользователей.
    """
    use_in_migrations = True

    def create_user(self, username, password):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, is_god=True):
        user = self.model(username=username, is_god=is_god)
        user.set_password(password)
        user.save()
        return user


# AccountModel используется для создания пользователей.
# Чтобы Django понял, что нужно использовать именно эту модель, 
# в файле qa/settings.py добавлен ключ AUTH_USER_MODEL = <appname.modelname>
class AccountModel(AbstractBaseUser):
    """
    Таблица с пользователями.
    """
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=256, null=False)
    is_god = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = AccountManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

