from django.contrib import admin
from .models import Practice

# Register your models here.
@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ['label','name','address','phone']
