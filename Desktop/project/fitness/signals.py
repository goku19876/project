from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Goal

# @receiver(post_save,sender=User)
# def create_goal(sender,instance,created,**kwargs):
#     if created:
#         Goal.objects.create(user=instance)

# @receiver(post_save,sender=User)
# def save_goal(sender,instance,**kwargs):
#     instance.goal.save()

# @receiver(request_finished,sender=User)
# def deleteGoal(sender,**kwargs):
#     print("deleted goal")