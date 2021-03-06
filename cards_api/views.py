from rest_framework.views import Response
from rest_framework import viewsets
from rest_framework import filters
from cards_api import serializers
from django.db.models import Q
from cards_api import models
import random
DEFAULT_PLAYER_CLASS = 'Neutral'
PLAYER_CLASS_LIST = ['Druid', 'Hunter', 'Mage', 'Paladin',
                     'Priest', 'Rogue', 'Shaman', 'Warlock', 'Warrior', 'Neutral']

class CardViewSet(viewsets.ViewSet):
  """Represent the Card ViewSet"""
  def list(self, request, format=None):
    player_class = request.query_params.get('player_class')
    if not player_class in PLAYER_CLASS_LIST or player_class is None:
      return Response({'errors': [{'key': 'player_class', 'message': 'Invalid player_class'}]}, status=400)
    queryset = models.Card.objects.filter(Q(player_class=player_class) | Q(player_class=DEFAULT_PLAYER_CLASS))
    cards = random.sample(list(queryset), 30)
    serializer = serializers.ListCardSerializer(cards, many=True)
    return Response(serializer.data)

