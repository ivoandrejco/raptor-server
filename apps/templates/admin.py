from django.contrib import admin
from .models import Investigation, Issue

# Register your models here.
@admin.register(Investigation)
class InvestigationAdmin(admin.ModelAdmin):
  list_display = ['id','title','json','tags','comment']

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
  list_display = ['id','title','json','differential','presentation','conclusion']
