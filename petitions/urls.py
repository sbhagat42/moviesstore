from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='petitions_index'),
    path('create/', views.create_petition, name='create_petition'),
    path('vote_yes/<int:petition_id>/', views.vote_yes, name='vote_yes'),
    path('vote_no/<int:petition_id>/', views.vote_no, name='vote_no'),
]
