from django.contrib import admin

# Register your models here.
from .models import Diagnosis

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display    = ['patient','kind','title','description']
    search_fields   = ["patient","title"]

    def patient(self,obj):
        return obj.pid
    
    

