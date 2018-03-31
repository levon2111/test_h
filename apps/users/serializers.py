import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers

from apps.core.serializer_fields import Base64ImageField
from apps.core.utils import generate_unique_key, send_email_job_registration
from apps.users.models import User, Test, TestQuestion, TestQuestionAnswers, Learner, TestResults
from apps.users.validators import check_valid_password


def base64_to_image(base64_string):
    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]

    base64_string = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)  # You can save this as file instance.
    return base64_string


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'user_images/' + filename


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    first_name = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )

    auth_type = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    last_name = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )

    address = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    image = Base64ImageField()
    zip_code = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    contact_person_name = serializers.CharField(
        required=False,
    )
    email = serializers.EmailField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    phone = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    modified = serializers.CharField(
        required=False,
    )
    url = serializers.HyperlinkedIdentityField(view_name="users-detail")

    class Meta:
        model = User
        exclude_password = ('password', 'repeat_password',)
        exclude_other_fields = ('is_superuser', 'is_staff', 'groups', 'user_permissions',)
        exclude = exclude_other_fields
        read_only_fields = ('token', 'last_login', 'created', 'modified', 'date_joined',)
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }

    def create(self, validated_data):
        validated_data.pop('repeat_password', None)
        validated_data['password'] = 'temporary_password'
        validated_data['token'] = generate_unique_key(validated_data['email'])
        # if validated_data['image']:
        #     validated_data['image'] = base64_to_image(validated_data['image'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.validate(validated_data)
        validated_data.pop('repeat_password', None)
        # if validated_data['image']:
        #     validated_data['image'] = base64_to_image(validated_data['image'])
        updated_object = super().update(instance, validated_data)
        if 'password' in validated_data:
            updated_object.set_password(validated_data['password'])
            updated_object.save()

        return updated_object

    def validate(self, data):
        email = data.get('email')
        if email and 'email' in data:
            data['email'] = email.lower()
            data['username'] = data['email']
        if 'email' in data:
            self.check_valid_email(data['email'], self.context['request'].user.pk)
        check_valid_password(data, user=self.context['request'].user)

        return data

    @staticmethod
    def check_valid_email(value, pk):
        old_user = User.objects.get(pk=pk)
        if User.objects.filter(email=value).exists() and old_user.email != value:
            raise serializers.ValidationError({'email': ['This email address has already exist.']})

        return value


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    @staticmethod
    def send_mail(validated_data):
        user = User.objects.get(email=validated_data['email'])
        user.reset_key = generate_unique_key(user.email)

        mail_name = ''
        if user.auth_type == 'company':
            mail_name = user.contact_person_name
        elif user.auth_type != 'corporate':
            mail_name = user.first_name
        else:
            mail_name = user.contact_person_name

        send_email_job_registration(
            'TEST',
            user.email,
            'reset_password',
            {
                'reset_key': user.reset_key,
                'name': mail_name
            },
            'Reset your password',
        )
        user.save()

    def validate(self, data):
        self.check_email(data['email'])

        return data

    @staticmethod
    def check_email(value):
        user = User.objects.filter(email=value)

        if not user.exists():
            raise serializers.ValidationError('This email address does not exist.')

        if not user.filter(is_active=True).exists():
            raise serializers.ValidationError('Your account is inactive.')

        return value


class SignUpSerializer(serializers.Serializer):
    USER_TYPE_CHOICES = (
        ('individual', 'Individual'),
        ('corporate', 'Corporate'),
        ('company', 'Company'),
    )

    email = serializers.EmailField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()
    auth_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)
    first_name = serializers.CharField(
        required=False,
        allow_blank=True,
    )
    last_name = serializers.CharField(
        required=False,
        allow_blank=True,
    )
    company_name = serializers.CharField(
        required=False,
        allow_blank=True,
    )
    contact_person_name = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    @staticmethod
    def save_user(validated_data):
        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        mail_name = ''

        user.auth_type = validated_data['auth_type']
        user.is_active = False
        user.email_confirmation_token = generate_unique_key(user.email)
        user.save()

        send_email_job_registration(
            'TEST',
            user.email,
            'account_confirmation',
            {
                'token': user.email_confirmation_token,
                'name': mail_name
            },
            'Welcome to TEST',
        )

    def validate(self, data):
        check_valid_password(data)
        self.check_valid_email(data['email'])

        return data

    @staticmethod
    def check_valid_email(value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError({'email': ['This email address has already exist.']})

        return value


class ConfirmAccountSerializer(serializers.Serializer):
    token = serializers.CharField()

    @staticmethod
    def confirm(validated_data):
        user = User.objects.get(email_confirmation_token=validated_data['token'])
        user.is_active = True
        user.email_confirmation_token = None
        user.save()

    def validate(self, data):
        if not User.objects.filter(email_confirmation_token=data['token']).exists():
            raise serializers.ValidationError('Invalid token.')

        return data


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    repeat_password = serializers.CharField()

    def reset(self, validated_data):
        user = User.objects.get(reset_key=self.context['reset_key'])
        user.set_password(validated_data['password'])
        user.reset_key = None
        user.save()

    def validate(self, data):
        check_valid_password(data)
        self.check_valid_token()

        return data

    def check_valid_token(self):
        if not User.objects.filter(reset_key=self.context['reset_key']).exists():
            raise serializers.ValidationError('Token is not valid.')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()

    def change_password(self, validated_data):
        self.validate(validated_data)
        user = User.objects.get(pk=self.context['id'])
        user.set_password(validated_data['password'])
        user.save()

    def validate(self, data):
        error = check_valid_password(data)
        if error:
            raise serializers.ValidationError({'email': error})
        self.check_valid_old_password(data)

        return data

    def check_valid_old_password(self, data):
        user = User.objects.get(pk=self.context['id'])
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({'password': ['Old password incorrect']})


class TestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(
        required=True,
        max_length=255,
        allow_blank=True,
    )

    class Meta:
        model = Test
        fields = '__all__'


class TestQuestionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    test = serializers.HyperlinkedRelatedField(
        queryset=Test.objects.all(),
        view_name='test-detail',
    )
    question = serializers.CharField(
        required=True,
        max_length=255,
        allow_blank=True,
    )

    class Meta:
        model = TestQuestion
        fields = '__all__'


class TestQuestionAnswersSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    question = serializers.HyperlinkedRelatedField(
        queryset=Test.objects.all(),
        view_name='testquestion-detail',
    )
    answer = serializers.CharField(
        required=True,
        max_length=255,
        allow_blank=True,
    )

    class Meta:
        model = TestQuestionAnswers
        fields = '__all__'


class TestResultsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    learner = serializers.HyperlinkedRelatedField(
        queryset=Learner.objects.all(),
        view_name='learner-detail',
    )
    test = serializers.HyperlinkedRelatedField(
        queryset=Test.objects.all(),
        view_name='test-detail',
    )
    question = serializers.HyperlinkedRelatedField(
        queryset=TestQuestion.objects.all(),
        view_name='testquestion-detail',
    )
    answer = serializers.HyperlinkedRelatedField(
        queryset=TestQuestionAnswers.objects.all(),
        view_name='testquestionanswers-detail',
    )

    class Meta:
        model = TestResults
        fields = '__all__'
