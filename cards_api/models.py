from django.db import models
import requests

class CardManager():
  """Mangaer for user Model """
  def create_card(self):
    """Create and save a new Card"""
    card = self.model( card_id= card_id, dbf_id= dbf_id, name=name, card_set=card_set, type= type, text=text, player_class=player_class, locale=locale)
    card.save(using=self._db)
    return card
class Card(models.Model):
  TEST = 'test'
  """Database model for cards in the system"""
  card_id = models.CharField(max_length=255, null=False)
  dbf_id = models.CharField(max_length=255, null=False)
  name = models.CharField(max_length=50, null=False)
  player_class = models.CharField(max_length=50, null=False)

  objects = CardManager()

  def __str__(self):
    """Return String representation for our user """
    return self.card_id

  @classmethod
  def load(cls):
    resp = requests.get(
        "https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/Rastakhan%27s%20Rumble", headers={"X-Mashape-Key": "ZTMJtzbYvXmshPTFEZI4ztIy3I68p1nPwgHjsnIGukKZeJxGcs"})
    cards = resp.json()
    for card in cards:
      print(card)
      print("========================================")
      card_id = card.get('cardId')
      dbf_id = card.get('dbfId')
      name = card.get('name')
      player_class = card.get('playerClass', '')
      cls.objects.create(card_id=card_id, dbf_id=dbf_id, name=name, player_class=player_class)

