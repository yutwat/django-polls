from django import forms

from .models import Question, Choice, Answer

# set forms.py example
class AnswerForm(forms.Form):

	class Meta:
		your_name = forms.CharField(label='Your name', max_length=100)
