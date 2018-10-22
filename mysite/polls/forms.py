from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory

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

class ChoiceForm(ModelForm):
	class Meta:
		model = Choice
		fields = ['choice_text']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['text']
