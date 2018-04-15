import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.models import AbstractBaseModel


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'user_images/' + filename


def get_file_portfolio_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'project_images/' + filename


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=False):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_active=is_active,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser, AbstractBaseModel):
    ROLE_CHOICES = (
        ('none', 'Without role'),
    )

    auth_type = models.CharField(
        max_length=255,
    )
    username = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    address = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    image = models.ImageField(
        upload_to=get_file_path,
        null=True,
        blank=True,
    )
    zip_code = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    contact_person_name = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    email = models.EmailField(unique=True)
    email_confirmation_token = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    reset_key = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    role = models.CharField(
        choices=ROLE_CHOICES,
        max_length=32,
        default='none',
    )

    phone = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Users'


class Learner(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Learner'


class Test(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Test'


class TestQuestion(AbstractBaseModel):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'TestQuestion'


class TestQuestionAnswers(AbstractBaseModel):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, null=False)
    correct = models.BooleanField(default=False)
    rate = models.IntegerField()

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name_plural = 'TestQuestionAnswer'


class TestResults(AbstractBaseModel):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(TestQuestionAnswers, on_delete=models.CASCADE)

    def __str__(self):
        return self.learner.name

    class Meta:
        verbose_name_plural = 'TestResults'


class TestAnalysisResults(AbstractBaseModel):
    rate_start = models.IntegerField()
    rate_end = models.IntegerField()
    analysis = models.TextField(null=False)

    def __str__(self):
        return self.analysis

    class Meta:
        verbose_name_plural = 'TestAnalysisResults'


class TestAnalysisTypeYesNo(AbstractBaseModel):
    rate_start = models.IntegerField()
    rate_end = models.IntegerField()
    analysis = models.TextField(null=False)

    def __str__(self):
        return self.analysis

    class Meta:
        verbose_name_plural = 'TestAnalysisTypeYesNo'
