from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(engine)
class EnginAdmin(admin.ModelAdmin):
    list_display = [field.name for field in engine._meta.fields]