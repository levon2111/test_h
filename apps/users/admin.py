from django.contrib import admin

from .models import User, Learner, Test


class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'is_active',
        'auth_type',
        'first_name',
        'last_name',
        'address',
        'phone',
    ]
    search_fields = ['email']
    list_editable = ['is_active']
    list_filter = ['is_active']

    class Meta:
        model = User


admin.site.register(User, UserModelAdmin)


class LearnerModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    search_fields = ['name']

    class Meta:
        model = Learner


admin.site.register(Learner, LearnerModelAdmin)


class TestModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    search_fields = ['name']

    class Meta:
        model = Test


admin.site.register(Test, TestModelAdmin)
