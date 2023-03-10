from django.contrib import admin

# Register your models here.
from questions import models
admin.site.register(models.Question)