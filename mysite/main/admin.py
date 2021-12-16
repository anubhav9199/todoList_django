# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Item)
