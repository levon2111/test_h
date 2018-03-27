"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from apps.core.urls import generate_url
from apps.users.views import UsersViewSet, TestViewSet, TestQuestionViewSet, TestQuestionAnswersViewSet
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='TEST API')

router = DefaultRouter()
router.register(r'users', UsersViewSet, base_name='users')
router.register(r'tests', TestViewSet, base_name='test')
router.register(r'test-questions', TestQuestionViewSet, base_name='testquestion')
router.register(r'test-questions-answer', TestQuestionAnswersViewSet, base_name='testquestionanswers')

urlpatterns = [
    url(r'^$', schema_view),
    generate_url('auth-users/', include('apps.users.urls', namespace='auth-users')),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

# urlpatterns = [
#
#     url(r'^api-auth/logout/', RedirectView.as_view(url='')),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^$', RedirectView.as_view(url=settings.API_VERSION_URL)),

#     url(r'^' + settings.API_VERSION_URL, include(router.urls, namespace='api')),
#     url(r'^' + settings.API_VERSION_URL + 'users/', include('apps.users.urls', namespace='users')),
#     url(r'^' + settings.API_VERSION_URL + 'core/', include('apps.core.urls', namespace='core')),
# ]
