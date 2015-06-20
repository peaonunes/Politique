from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class TipoParceria(models.Model):
	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	
	def __str__(self):
		return self.nome
	
	class  Meta:
		ordering = ('nome',)