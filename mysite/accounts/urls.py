from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path(r'signup/', views.signup, name='signup'),
]

# path('<int:question_id>/vote/', views.ResultsView.vote, name='vote'),