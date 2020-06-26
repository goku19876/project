# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid
from multiselectfield import MultiSelectField
#from django.shortcuts import get_object_or_404
# from main.models import Exercise as Exercise

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

class Routine(models.Model):
    name = models.CharField(auto_created=True, null=True,max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    exercises = models.ManyToManyField('main.Exercise',related_name='routines')
    #exercises = MultiSelectField(choices=exercise_choices)
    def __str__(self):
        return str(self.name)
    
    

