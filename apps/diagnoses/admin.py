from django.contrib import admin
from django.utils.html import mark_safe

# Register your models here.
from .models import Diagnosis, Investigation

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display    = ['patient','kind','title','description_html']
    search_fields   = ["patient","title"]

    def patient(self,obj):
        return obj.patient
    
    def description_html( self, obj ):
        return mark_safe( obj.description )

@admin.register(Investigation)
class InvestigationAdmin(admin.ModelAdmin):
    list_display = ['patient','title','created_on']
  
    def patient(self,obj):
        return obj.diagnosis.patient

    def title( self, obj ):
        return obj.template.title
