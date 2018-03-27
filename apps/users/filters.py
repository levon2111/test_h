import rest_framework_filters as filters

from apps.core.filters import BaseFilter
from .models import (
    User, Test, TestQuestion)


class UserFilter(filters.FilterSet, BaseFilter):
    created = filters.DateFilter(name='created', method='filter_created')

    class Meta:
        model = User
        fields = {
            'first_name': ['icontains', ],
            'last_name': ['icontains', ],
        }


class TestFilter(filters.FilterSet, BaseFilter):
    created = filters.DateFilter(name='created', method='filter_created')

    class Meta:
        model = Test
        fields = {
            'name': ['icontains', ],
        }


class TestQuestionFilter(filters.FilterSet, BaseFilter):
    created = filters.DateFilter(name='created', method='filter_created')

    class Meta:
        model = TestQuestion
        fields = {
            'test__name': ['icontains', ],
        }
