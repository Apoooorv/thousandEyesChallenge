# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SlowQueries(models.Model):
    endPoint = models.CharField(max_length=100, null=False, blank=False)
    time = models.DecimalField(decimal_places=2, max_digits=5)

class Queries(models.Model):
    endPoint = models.CharField(max_length=100, null=False, blank=False)
    count = models.IntegerField()