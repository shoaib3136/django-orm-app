from django.db import models
from django.contrib import admin
# Create your models here.
class Mobile(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    pieceno = models.CharField(max_length=100,primary_key=True)
    ram = models.CharField(max_length=50)
    cost = models.IntegerField()

class MobileAdmin(admin.ModelAdmin):
    list_display = ('pieceno','brand','model','ram','cost')

