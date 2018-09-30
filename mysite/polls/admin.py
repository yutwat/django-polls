from django.contrib import admin
from .models import  Question, Choice, Solution, Comment
from .forms import QuestionForm

class CommentInline(admin.TabularInline):
	model = Comment
	extra = 0

class SolutionInline(admin.TabularInline):
	model = Solution
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


# ---This is an old script---
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	fieldsets = [
	(None,			   {'fields': ['question_text', 'description', 'week_num', 'release_flag']}),
	('Date information', {'fields': ['pub_date', 'release_date'], }),
	]
	inlines = [ChoiceInline, SolutionInline, CommentInline]
	list_filter = ['pub_date', 'release_date']
	search_fields = ['question_text', 'description', 'week_num', 'release_flag']

admin.site.register(Question, QuestionAdmin)
# ------

