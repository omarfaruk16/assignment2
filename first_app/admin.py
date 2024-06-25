from django.contrib import admin
from .models import TodoModel,FormModel



admin.site.register(FormModel)
admin.site.register(TodoModel)