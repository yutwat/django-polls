from django import forms
from django.forms import ModelForm

from .models import Question, Choice, Solution, Comment


# user answer form
class SolutionForm(ModelForm):
	# your_answer = forms.CharField(label='Your answer: ', required=True, max_length=100)
	class Meta:
		model = Solution
		fields = ['solution_text', 'description',]


# user answer form
class QuestionForm(ModelForm):
	# your_answer = forms.CharField(label='Your answer: ', required=True, max_length=100)
	class Meta:
		model = Question
		fields = ['question_text', 'description']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['text']
