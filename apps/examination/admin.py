from django.contrib import admin

from .models import Examination

# Register your models here.
@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    list_display = ['patient','collected_on','weight','height','BMI','IBW','ABW','BSA_D','BSA_M','BP','pulse']

    def patient(self,obj):
        return obj.consultation.patient

