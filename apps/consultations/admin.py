from django.contrib import admin
from .models import Consultation, Issue, Investigation, Letter

from diagnoses.models import Diagnosis

# Register your models here.
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
  list_display = ['patient','code','created_on','provider']

  def patient(self,obj):
    return obj.pid
  

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
  list_display = ['patient','created_on','title','presentation', 'created_on']

  def created_on(self,obj):
    return obj.cid.created_on
  
  def patient(self,obj):
    return obj.cid.pid

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
  list_display = ['patient','consultation','title','status','created_on']

  def consultation(self,obj):
    return obj.cid
  
  def patient(self,obj):
    return obj.cid.pid

@admin.register(Investigation)
class InvestigationAdmin(admin.ModelAdmin):
  list_display = ['patient','issue','title','created_on']
  
  def issue(self,obj):
    return obj.iid

  def patient(self,obj):
    return obj.iid.cid.pid
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    print(db_field)
    if db_field.name == "diagnosis":
        kwargs["queryset"] = Diagnosis.objects.filter()
    return super().formfield_for_foreignkey(db_field, request, **kwargs)
