from django.contrib import admin

# Register your models here.
from tasks.models import tasks

admin.site.register(tasks)
