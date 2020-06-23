# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    goal = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now )

    def __str__(self):
        return self.goal

    def save(self):
        super(Goal,self).save()