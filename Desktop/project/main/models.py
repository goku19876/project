# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField





# Create your models here.
class Exercise(models.Model):
    equipment_choices = [
        ('BARBELL','Barbell'),
        ('DUMBBELL','Dumbbell'),
        ('KETTLEBELL','Kettlebell'),
        ('PULLUPBAR','Pullup Bar'),
        ('FOAMROLLER','Foam roller'),
        ('PLATES','Plates'),
        ]
    name = models.CharField(max_length=20,null=True)
    description = models.CharField(max_length=100,null=True)
    equipment_needed = MultiSelectField(choices=equipment_choices)

    def __str__(self):
        return self.name
        



# class Routine(models.Model):
#     name = models.CharField(max_length=100,default="{user}'s workout".format(user=User))
#     BEGINNER = 'Beginner'
#     ADVANCED = 'ADVANCED'
#     INTERMEDIATE='Intermediate'
#     level_choices = [
#         (BEGINNER, 'Beginner'),
#         (INTERMEDIATE,'Intermediate'),
#         (ADVANCED,'Advanced')
#     ]
#     user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
#     skill_level = models.CharField(max_length=10,choices=level_choices,default=BEGINNER)
#     activity = models.ForeignKey(Activity,default="activity")

#     #activity = models.ForeignKey(Activity)




    
    
