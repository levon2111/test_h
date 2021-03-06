from django.conf import settings
from django.core import serializers
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.users.filters import UserFilter, TestFilter, TestQuestionFilter, TestQuestionAnswersFilter, TestResultsFilter
from apps.users.models import User, Test, TestQuestion, TestQuestionAnswers, TestResults, Learner
from apps.users.serializers import (
    ForgotPasswordSerializer, SignUpSerializer,
    ConfirmAccountSerializer, ResetPasswordSerializer, ChangePasswordSerializer, UserSerializer, TestSerializer,
    TestQuestionSerializer, TestQuestionAnswersSerializer, TestResultsSerializer)


class Login(ObtainAuthToken):
    def get_serializer(self):
        return self.serializer_class()

    def post(self, request, *args, **kwargs):
        """
        ---
        serializer: AuthTokenSerializer
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        if not serializer.is_valid():
            return Response({
                'error': serializer.errors['non_field_errors'][0]
            }, status=status.HTTP_412_PRECONDITION_FAILED)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        image_user = ''
        if user.image:
            image_user = settings.BASE_URL + user.image.url

        return Response({
            'id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'auth_type': user.auth_type,
            'address': user.address,
            'image': image_user,
            'zip_code': user.zip_code,
            'contact_person_name': user.contact_person_name,
            'email': user.email,
            'phone': user.phone,
            'last_login': user.last_login,
            'is_active': user.is_active,
            'date_joined': user.date_joined,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
            'username': user.username,
            'token': token.key,
        })


class ForgotPasswordAPIView(APIView):
    serializer_class = ForgotPasswordSerializer

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        """
        ---
        request_serializer: ForgotPasswordSerializer
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.send_mail(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )
        error = serializer.errors
        if serializer.errors and hasattr(serializer.errors, 'non_field_errors'):
            error = {
                "email": serializer.errors['non_field_errors'][0]
            }

        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class SignUpAPIView(APIView):
    serializer_class = SignUpSerializer

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        """
        ---
        request_serializer: SignUpSerializer
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save_user(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(APIView):
    serializer_class = ResetPasswordSerializer

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request, reset_key):
        """
        ---
        request_serializer: ResetPasswordSerializer
        """

        context = {
            'request': request,
            'reset_key': reset_key,
        }
        user = User.objects.get(reset_key=context['reset_key'])
        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.reset(serializer.data)
            return JsonResponse(
                {
                    'email': user.email,
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(APIView):
    serializer_class = ChangePasswordSerializer

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        context = {
            'request': request,
            'id': request.user.id
        }
        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.change_password(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmAccountAPIView(APIView):
    serializer_class = ConfirmAccountSerializer

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        """
        ---
        request_serializer: ConfirmAccountSerializer
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.confirm(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, context):
        user = User.objects.filter(pk=self.request.user.pk)
        serializer = self.serializer_class(data=self.request.data)
        serializer.user = self.request.user
        print(serializers.serialize("json", user))
        if serializer.is_valid():
            return JsonResponse(
                {
                    'result': 'success',
                    'user': serializers.serialize("json", user)
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-updated_at')
    serializer_class = UserSerializer
    http_method_names = ['get', 'delete', 'post', 'put', 'patch', ]
    permission_classes = []
    filter_class = UserFilter
    search_fields = ('first_name', 'last_name', 'email', 'id',)
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    exclude_report_fields = ('password', 'last_login',)


class TestViewSet(ModelViewSet):
    queryset = (
        Test.objects
            .all()
            .order_by('-updated_at')
    )
    serializer_class = TestSerializer
    http_method_names = ['get', 'delete', 'post', 'put', 'patch', ]
    permission_classes = []
    filter_class = TestFilter
    search_fields = ('name',)
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)


class TestQuestionViewSet(ModelViewSet):
    queryset = (
        TestQuestion.objects
            .all()
            .order_by('-updated_at')
    )
    serializer_class = TestQuestionSerializer
    http_method_names = ['get', 'delete', 'post', 'put', 'patch', ]
    permission_classes = []
    filter_class = TestQuestionFilter
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)


class TestQuestionAnswersViewSet(ModelViewSet):
    queryset = (
        TestQuestionAnswers.objects
            .all()
            .order_by('-updated_at')
    )
    serializer_class = TestQuestionAnswersSerializer
    http_method_names = ['get', 'delete', 'post', 'put', 'patch', ]
    permission_classes = []
    filter_class = TestQuestionAnswersFilter
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)


class TestResultsViewSet(ModelViewSet):
    queryset = (
        TestResults.objects
            .all()
            .order_by('-updated_at')
    )
    serializer_class = TestResultsSerializer
    http_method_names = ['get', 'delete', 'post', 'put', 'patch', ]
    permission_classes = []
    filter_class = TestResultsFilter
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)


class GetTestAPIView(APIView):
    permission_classes = []

    def get(self, context, test_id):
        test = get_object_or_404(Test, pk=test_id)
        questions = []
        test_questions = TestQuestion.objects.filter(test=test)
        for x in test_questions:
            answers = []
            questions_answers = TestQuestionAnswers.objects.filter(question=x)
            for y in questions_answers:
                answers.append({
                    'id': y.pk,
                    'answer': y.answer,
                    'correct': y.correct,
                    'rate': y.rate,
                })
            questions.append({'id': x.pk, 'question': x.question, 'answers': answers})
        return JsonResponse(
            {
                'status_code': 200,
                'results': {
                    'test': {
                        'id': test.pk,
                        'name': test.name
                    },
                    'questions': questions
                }
            },
            status=status.HTTP_200_OK,
        )


class TestAPIView(APIView):
    def post(self, request):
        data = request.data
        learner = Learner(name=data['learner'])
        learner.save()
        for x in data['result']:
            test_result = TestResults(
                test=Test.objects.get(pk=x['test_id']),
                learner=learner,
                question=TestQuestion.objects.get(pk=x['question_id']),
                answer=TestQuestionAnswers.objects.get(pk=x['answer_id'])
            )
            test_result.save()

        return Response('success', status=status.HTTP_201_CREATED)

