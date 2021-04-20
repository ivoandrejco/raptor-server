from django.contrib import admin

from .models import Consultation, Letter, Examination

# Register your models here.
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
  list_display = ['patient','code','created_on','provider']

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
  list_display = ['patient','consultation','title','status','created_on']

  def consultation(self,obj):
    return obj.cid
  
  def patient(self,obj):
    return obj.cid.patient

@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    list_display = ['patient','collected_on','weight','height','BMI','IBW','ABW','BSA_D','BSA_M','BP','pulse']

    def patient(self,obj):
        return obj.consultation.patient

