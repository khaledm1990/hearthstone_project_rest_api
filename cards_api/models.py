from django.db import models


class CardManager():
  """Mangaer for user Model """
  def create_card(self):
    """Create and save a new Card"""
    card = self.model( card_id= card_id, dbf_id= dbf_id, name=name, card_set=card_set, type= type, text=text, player_class=player_class, locale=locale)
    card.save(using=self._db)
    return card
class Card(models.Model):
  """Database model for cards in the system"""
  card_id = models.CharField(max_length=255, null=False)
  dbf_id = models.CharField(max_length=255, null=False)
  name = models.CharField(max_length=50, null=False)
  card_set = models.CharField(max_length=500, null=False)
  type = models.CharField(max_length=50, null=False)
  text = models.TextField(max_length=255)
  player_class = models.CharField(max_length=50, null=False)
  locale = models.CharField(max_length=50, null=False)

  objects = CardManager()

  def __str__(self):
    """Return String representation for our user """
    return self.card_id
