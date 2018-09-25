from django import forms
from django.forms import ModelForm

from .models import Question, Choice, Answer


# user answer form
class AnswerForm(ModelForm):
	# your_answer = forms.CharField(label='Your answer: ', required=True, max_length=100)
	class Meta:
		model = Answer
		fields = ['answer_text', 'description',]


# user answer form
class QuestionForm(ModelForm):
	# your_answer = forms.CharField(label='Your answer: ', required=True, max_length=100)
	class Meta:
		model = Question
		fields = ['question_text', 'description']
