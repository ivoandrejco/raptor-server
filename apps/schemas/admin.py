from django.contrib import admin
from .models import Schema

# Register your models here.
@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
  list_display = ['id','kind','title','json','ordering']

