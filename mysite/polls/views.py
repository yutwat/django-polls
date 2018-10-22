from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

from .models import Question, Choice, Solution, Comment
from .forms import SolutionForm, QuestionForm, ChoiceForm, CommentForm

class QuestionListView(generic.ListView):
	# context_object_name = 'latest_question_list'
	# context_object_name = 'question_list'
	paginate_by = 10

	def get_queryset(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('pub_date')[:5]

class QuestionDetailView(generic.DetailView):
	model = Question
	form_class = CommentForm

class CommentCreateView(generic.CreateView):
	model = Question
	form_class = QuestionForm
	context_object_name = 'question_list'
	# template_name = 'polls/create.html'
	success_url = reverse_lazy('question_list')  # redirect url when it succeeds.

	# return render(request, template_name, {'form': form})

	def form_valid(self, form):
		result = super().form_valid(form)
		messages.success(
			self.request, '"{}" was successfully created.'.format(form.instance))
		return result

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_question_detail.html', {'post': post})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/question_detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		
		if str(selected_choice) == str(question.solution_set.get()):
			return render(request, 'polls/question_detail.html', {
				'user_name': request.user.username, 
				'question': question,
				'selected_choice': selected_choice,
				'answer': question.solution_set.get(),
				'answer_description': question.solution_set.get(),
				'correct_message': 'Correct!',
			})
		else:
			return render(request, 'polls/question_detail.html', {
				'question': question,
				'selected_choice': selected_choice,
				'answer': question.solution_set.get(),
				'incorrect_message': 'Incorrect..',
			})

def post_new(request, pk):
	question = get_object_or_404(Question, pk=pk)
	if request.method == "POST":
		form = SolutionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('question_detail', pk=post.pk)
	else:
		form = SolutionForm()
	return render(request, 
		'polls/post_edit.html', {
		'form': form, 
		'question': question,
		})

# added for forms.py
def post_edit(request, pk):
	question = get_object_or_404(Question, pk=pk)
	post = get_object_or_404(Solution, pk=pk)

	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		# form = SolutionForm(request.POST)
		form = SolutionForm(request.POST, instance=post)
		# check whether it's valid:
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.published_date = 	timezone.now()
			post.save()
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return redirect('polls:question_detail', pk=post.pk)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = SolutionForm(instance=post)

	return render(request, 
		'polls/post_edit.html', {
		'form': form, 
		'post': post, 
		'question': question,
		})

# show your answer input pagex	
def your_answer(request, pk):
	question = get_object_or_404(Question, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			post = form.save(commit=False)
			post.name = request.user
			post.target = question

			# scoring
			if str(post.text)==str(question.solution_set.get()):
				post.score = 1
			else:
				post.score = 0

			post.save()

			# redirect to a new URL:
			return redirect('polls:your_answer', pk=question.id)
	
	# if a GET (or any other method) we'll create a blank form
	else:
		form = CommentForm()

	return render(request, 
		'polls/answer.html', {
		'form': form, 
		'question': question,
		'solution': str(question.solution_set), 
		})


# pagination
def _get_page(list_, page_no, count=1):

	paginator = Paginator(list_, count)
	try:
		page = paginator.page(page_no)
	except (EmptyPage, PageNotAnInteger):
		page = paginator.page(1)
	return page
 
