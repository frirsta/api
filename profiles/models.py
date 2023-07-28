from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from api import settings


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, password, first_name, last_name, is_client, is_tester):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',
                              max_length=150, unique=True)
    username = models.CharField(max_length=150, blank=False, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name='first_name', max_length=100)
    last_name = models.CharField(verbose_name='last_name', max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' - ' + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class TestRequirements(models.Model):
    conclusion = models.TextField(blank=False)
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='test_as_client', on_delete=models.CASCADE)
    tester = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='test_as_tester')


class Test(models.Model):
    test = models.ForeignKey(TestRequirements, on_delete=models.CASCADE)
    testers = models.ManyToManyField(User)
    conclusion = models.TextField(blank=False)


class TesterResult(models.Model):
    conclusion = models.TextField(blank=False)


class Result(models.Model):
    conclusion = models.TextField(blank=False)
