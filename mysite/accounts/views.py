from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect

from .models import User
from .forms import SignUpForm

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/polls/')
	else:
		form = SignUpForm()
	return render(request, 'accounts/signup.html', {'form': form})