from rest_framework import serializers
from cards_api import models


class CardSerializer(serializers.ModelSerializer):
  """Serializes a Card object"""
  class Meta:
    model = models.Card
    fields = ['dbf_id', 'name', 'player_class']
