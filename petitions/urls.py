from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='petitions_index'),
    path('create/', views.create_petition, name='create_petition'),
    path('<int:petition_id>/vote_yes/', views.vote_yes, name='vote_yes'),
    path('<int:petition_id>/vote_no/', views.vote_no, name='vote_no'),
]