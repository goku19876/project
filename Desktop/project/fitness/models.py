# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid
from django.shortcuts import get_object_or_404

# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    goal = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    
    def __str__(self):
        return self.goal

    def save(self):
        super(Goal,self).save()
    

