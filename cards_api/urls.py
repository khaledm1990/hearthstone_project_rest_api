from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cards_api import views


router = DefaultRouter()
router.register('cards', views.CardViewSet, base_name='cards')

urlpatterns = [
  path('', include(router.urls))
]
