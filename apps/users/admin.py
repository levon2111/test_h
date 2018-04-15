from django.contrib import admin

from .models import User, Learner, Test, TestQuestion, TestQuestionAnswers, TestResults, TestAnalysisResults, \
    TestAnalysisTypeYesNo


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


class TestQuestionModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'test',
        'question',
    ]
    search_fields = ['test', 'question']

    class Meta:
        model = TestQuestion


admin.site.register(TestQuestion, TestQuestionModelAdmin)


class TestQuestionAnswersModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'answer',
        'question',
        'correct',
    ]
    search_fields = ['answer', 'question']

    class Meta:
        model = TestQuestionAnswers


admin.site.register(TestQuestionAnswers, TestQuestionAnswersModelAdmin)


class TestAnalysisResultsModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'rate_start',
        'rate_end',
        'analysis',
    ]
    search_fields = []

    class Meta:
        model = TestAnalysisResults


admin.site.register(TestAnalysisResults, TestAnalysisResultsModelAdmin)


class TestAnalysisTypeYesNoModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'rate_start',
        'rate_end',
        'analysis',
    ]
    search_fields = []

    class Meta:
        model = TestAnalysisTypeYesNo


admin.site.register(TestAnalysisTypeYesNo, TestAnalysisTypeYesNoModelAdmin)


class TestResultsModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'learner',
        'test',
        'question',
        'answer',
        'correct_answer',
        'answer_rate',
    ]
    search_fields = ['learner', 'test']
    list_filter = ['test', 'learner']
    ordering = ['test', 'learner', ]

    def correct_answer(self, obj):
        return obj.answer.correct

    def answer_rate(self, obj):
        return obj.answer.rate

    class Meta:
        model = TestResults


admin.site.register(TestResults, TestResultsModelAdmin)
