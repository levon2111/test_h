from django.contrib import admin

from .models import User, Learner, Test, TestQuestion, TestQuestionAnswers, TestResults, TestSandxak, TestAnalysis


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


class TestSandxakModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    search_fields = ['name']

    class Meta:
        model = TestSandxak


admin.site.register(TestSandxak, TestSandxakModelAdmin)


class TestQuestionModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'test',
        'question',
        'sandxak',
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


#
# class TestAnalysisResultsModelAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'rate_start',
#         'rate_end',
#         'analysis',
#     ]
#     search_fields = []
#
#     class Meta:
#         model = TestAnalysisResults
#
#
# admin.site.register(TestAnalysisResults, TestAnalysisResultsModelAdmin)


# class TestAnalysisTypeYesNoModelAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'rate_start',
#         'rate_end',
#         'analysis',
#     ]
#     search_fields = []
#
#     class Meta:
#         model = TestAnalysisTypeYesNo
#
#
# admin.site.register(TestAnalysisTypeYesNo, TestAnalysisTypeYesNoModelAdmin)

class TestAnalysisModelAdmin(admin.ModelAdmin):
    list_display = [
        'yes_no_rate_end',
        'yes_no_rate_start',
        'type_two_rate_end',
        'type_two_rate_start',
        'analysis',
    ]
    search_fields = []

    class Meta:
        model = TestAnalysis


admin.site.register(TestAnalysis, TestAnalysisModelAdmin)


class TestResultsModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'learner',
        'test',
        'question',
        'answer',
        'correct_answer',
        'answer_rate',
        'sandxak',
        'analysis',
    ]
    search_fields = ['learner', 'test']
    list_filter = ['test', 'learner__name']
    ordering = ['test', 'learner', ]

    def sandxak(self, obj):
        return obj.question.sandxak.name

    def analysis(self, obj):
        rating = TestResults.objects.filter(learner=obj.learner, test=obj.test)
        sumYes = 0
        sumOne = 0
        countKexciq = 0

        for x in rating:
            if x.question.sandxak.name == '1':
                sumOne = sumOne + x.answer.rate
            if x.question.sandxak.name == '2':
                sumYes = sumYes + x.answer.rate
            if x.question.sandxak.name == 'kexciq':
                countKexciq = countKexciq+1

        if countKexciq > 5:
            return 'Kexciq'
        an = TestAnalysis.objects.filter(
            yes_no_rate_end__gte=sumYes,
            yes_no_rate_start__lte=sumYes,
            type_two_rate_end__gte=sumOne,
            type_two_rate_start__lte=sumOne
        )
        if len(an):
            return an.first().analysis
        return ''

    def correct_answer(self, obj):
        return obj.answer.correct

    def answer_rate(self, obj):
        return obj.answer.rate

    class Meta:
        model = TestResults


admin.site.register(TestResults, TestResultsModelAdmin)
