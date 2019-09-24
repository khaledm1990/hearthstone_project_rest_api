from django.urls import path
from cards_api import views

urlpatterns = [
  path('cards/', views.CardApiView.as_view()),
]
