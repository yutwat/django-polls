import os
import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django import forms

# from accounts.models import User

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
	week_num = models.CharField(
		verbose_name=_("week"),
		max_length=50, 
		blank=False, 
		default='week0', 
		help_text=_("week number")
		)
	release_flag = models.BooleanField(
		default=False,
		help_text=_("release or not"),
		)
	release_date = models.DateTimeField(
		'release date', 
		null=True,
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
	descriptive = forms.CharField(
		label='Answer', 
		max_length=50,
		)

	def __str__(self):
		return self.choice_text 


class Solution(models.Model):
	
	question = models.ForeignKey(
		Question, 
		on_delete=models.CASCADE
		)
	solution_text = models.CharField(
		max_length=200
		)
	description = models.TextField(
		verbose_name=_("Description"),
		blank=True, 
		help_text=_("a description of the answer")
		)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	# ...
	def __str__(self):
		return self.solution_text 
