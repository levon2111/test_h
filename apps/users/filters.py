import rest_framework_filters as filters
from apps.core.filters import BaseFilter

from .models import (
    User)


class UserFilter(filters.FilterSet, BaseFilter):
    created = filters.DateFilter(name='created', method='filter_created')

    class Meta:
        model = User
        fields = {
            'first_name': ['icontains', ],
            'last_name': ['icontains', ],
        }
