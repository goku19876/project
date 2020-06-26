# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Goal, Routine
from django.contrib import admin


# Register your models here.
admin.site.register(Goal)
admin.site.register(Routine)