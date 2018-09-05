import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django import forms

class Question(models.Model):

	question_text = models.CharField(
		verbose_name=_("Question_text"),
		max_length=200, 
		blank=False
		)
	description = models.TextField(
		verbose_name=_("Description"),
		blank=True, 
		help_text=_("a description of the quiz")
		)
	pub_date = models.DateTimeField(
		'date published'
		)

	def __str__(self):
		 return self.question_text

	def was_published_recently(self):
		 now = timezone.now()
		 return now - datetime.timedelta(days=1) <= self.pub_date <= now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
		

class Choice(models.Model):
	
	question = models.ForeignKey(
		Question, 
		on_delete=models.CASCADE
		)
	choice_text = models.CharField(
		max_length=200
		)
	votes = models.IntegerField(
		default=0
		)

	# ...
	def __str__(self):
		return self.choice_text 


class Descriptive(forms.Form):

	answer_field = forms.CharField(
		label='Answer', 
		max_length=50,
		)

	def clean_answer(self):
		answer = self.cleaned_data['answer']
		return answer


# added on 8-31-2018
# descriptive answer form
class Answer(models.Model):
	
	question = models.ForeignKey(
		Question, 
		on_delete=models.CASCADE
		)
	answer_text = models.CharField(
		max_length=200
		)
	description = models.TextField(
		verbose_name=_("Description"),
		blank=True, 
		help_text=_("a description of the answer")
		)

	# ...
	def __str__(self):
		return self.answer_text 
