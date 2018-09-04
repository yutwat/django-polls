import datetime

from django.db import models
from django.utils import timezone
from django_markdown.models import MarkdownField

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	question_description = models.TextField(blank=True)
	# question_description = MarkdownField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		 return self.question_text

	def was_published_recently(self):
		 now = timezone.now()
		 return now - datetime.timedelta(days=1) <= self.pub_date <= now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
		

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	# ...
	def __str__(self):
		return self.choice_text 


# added on 8-31-2018
# descriptive answer form
class Descriptive(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	descriptive_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	# ...
	def __str__(self):
		return self.descriptive_text 
