from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

from .models import Question, Choice, Answer
from .forms import AnswerForm


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'



# ###############

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# ###############


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		
		if str(selected_choice) == str(question.answer_set.get()):
			return render(request, 'polls/detail.html', {
				'user_name': request.user.email, 
				'question': question,
				'selected_choice': selected_choice,
				'answer': question.answer_set.get(),
				'answer_description': question.answer_set.get(),
				'correct_message': 'Correct!',
			})
		else:
			return render(request, 'polls/detail.html', {
				'question': question,
				'selected_choice': selected_choice,
				'answer': question.answer_set.get(),
				'incorrect_message': 'Incorrect..',
			})


		form = AnswerForm(request.Post)
		return render(request, 'polls:deatil', {'form': form})

		# return HttpResponseRedirect(reverse('polls:check', args=(question.id,)))
		

# pagination
def _get_page(list_, page_no, count=1):
    
    paginator = Paginator(list_, count)
    try:
        page = paginator.page(page_no)
    except (EmptyPage, PageNotAnInteger):
        page = paginator.page(1)
    return page
 
 
def index(request):
    
    page = _get_page(Message.objects.all(), request.GET.get('page'))
    d = {
        "page":page,
        }
    return render(request, 'page/index.html', d)