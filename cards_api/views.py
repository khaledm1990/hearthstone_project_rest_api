from rest_framework.views import Response
from rest_framework import viewsets
from rest_framework import filters
from cards_api import serializers
from cards_api import models


class CardViewSet(viewsets.ViewSet):
  """Represent the Card ViewSet"""

  def list(self, request, format=None):
    player_class = request.query_params.get('player_class', 'Neutral')[:30]
    queryset = models.Card.objects.filter(player_class=player_class)
    serializer = serializers.ListCardSerializer(queryset, many=True)
    return Response(serializer.data)
