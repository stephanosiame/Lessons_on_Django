from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path("specifics/<int:question_id>/", views.Detail, name = 'detail'),
    path("<int:question_id/results/", views.Result, name = 'result'),
    path('<int:question_id/vote/', views.Vote, name = 'vote')
    ]