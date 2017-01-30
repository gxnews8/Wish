from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length = 255)
    l_name = models.CharField(max_length = 255)

class Item(models.Model):
    name = models.CharField(max_length = 255)
    create_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)

class Wish(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
