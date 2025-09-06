from django.contrib import admin

# Register your models here.
from .models import question, Choices

admin.site.register(question)
admin.site.register(Choices)