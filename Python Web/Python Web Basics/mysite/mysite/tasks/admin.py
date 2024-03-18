from django.contrib import admin

from mysite.tasks.models import Task

admin.site.register(Task)
