# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime

class Client(models.Model):
    nom=models.CharField(max_length=200)
    cif=models.CharField(max_length=20)
    adreca=models.CharField(max_length=100)
    telefon=models.CharField(max_length=20)
    
class Familia_Article(models.Model):
    class Meta:
        verbose_name="Família d'article"
        verbose_name_plural="Famílies d'articles"
    
    descripcio=models.CharField(max_length=200)
    
class Article(models.Model):
    
    class Meta:
        verbose_name_plural="Articles"
    
    familia=models.ForeignKey(Familia_Article)
    descripcio=models.CharField(max_length=200)

class Stock(models.Model):
    article=models.ForeignKey(Article)
    quantitat=models.FloatField()
    
class Preu(models.Model):
    article=models.ForeignKey(Article)
    valor=models.FloatField()
    data_inicial= models.DateTimeField()
    data_final= models.DateTimeField(blank=True)
class Compra(models.Model):
    client=models.ForeignKey(Client)
    data=models.DateTimeField()
class DetallCompra(models.Model):
    article=models.ForeignKey(Article)
    preu=models.ForeignKey(Preu)
    quantitat=models.FloatField()
    
    
    
    
    

