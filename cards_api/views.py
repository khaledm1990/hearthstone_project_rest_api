from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
# Create your views here.


class CardApiView(APIView):
  """Represent the Crd APIView"""
  def get(self, request, format=None):
    """ Returns list of cards cards"""
    cards = ["cards1", "card2", "card3", "card4"]

    return Response({'success': True, 'cards': cards})
