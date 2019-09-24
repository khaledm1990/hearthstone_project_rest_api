from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

from rest_framework import viewsets

from cards_api import serializers
from cards_api import models


class CardViewSet(viewsets.ModelViewSet):
  """Represent the Card ViewSet"""

  serializer_class = serializers.CardSerializer
  query_set = models.Card.objects.all()

  # def get(self, request, format=None):
  #   """Returns list of cards"""
  #   cards = ["cards1", "card2", "card3", "card4"]

  #   return Response({'success': True, 'cards': cards})

  # def post(self, request):
  #   """Create a card """
  #   serializer = self.serializer_class(data=request.data)

  #   if serializer.is_valid():
  #     name = serializer.validated_data.get('name')
  #     result = f'New name called {name}'
  #     return Response({'success': True, 'result': result})
  #   else:
  #     return Response(
  #       serializer.errors,
  #       status=status.HTTP_400_BAD_REQUEST
  #     )