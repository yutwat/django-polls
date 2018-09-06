from django.contrib import admin
from .models import Question, Choice, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	fieldsets = [
	(None,               {'fields': ['question_text', 'description']}),
	('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline, AnswerInline]
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)