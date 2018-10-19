from django.urls import path
from django.views.generic import ListView
from .models import Question

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/create/', views.CommentCreateView.as_view(), name='create'),
    path('<int:question_id>/result/', views.vote, name='result'),
    path('<int:pk>/new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path(r'listview/', 
    	ListView.as_view(
    		queryset=Question.objects.all(), 
    		template_name='polls/about.html'), 
    	name='index_view'),
    path('<int:pk>/answer/', views.your_answer, name='your_answer'), 
]

# path('<int:question_id>/vote/', views.ResultsView.vote, name='vote'),