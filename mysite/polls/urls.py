from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.QuestionListView.as_view(), name='question_list'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('<int:pk>/create/', views.CommentCreateView.as_view(), name='create'),
    path('<int:question_id>/result/', views.vote, name='result'),
    path('<int:pk>/answer/', views.your_answer, name='your_answer'), 
]