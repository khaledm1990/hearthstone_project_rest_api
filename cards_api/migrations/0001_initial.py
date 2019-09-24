# Generated by Django 2.2.5 on 2019-09-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Card',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('card_id', models.CharField(max_length=255)),
				('dbf_id', models.CharField(max_length=255)),
				('name', models.CharField(max_length=50)),
				('card_set', models.CharField(max_length=500)),
				('type', models.CharField(max_length=50)),
				('text', models.TextField(max_length=255)),
				('player_class', models.CharField(max_length=50)),
				('locale', models.CharField(max_length=50)),
			],
		),
	]