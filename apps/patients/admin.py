from datetime import date
from django.contrib import admin

# Register your models here.
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
  list_display = ['name','dob','age','gender']

  def name(self,obj):
    return f'{obj.fname} {obj.lname}'

  def age(self,obj):
    today = date.today()
    return today.year - obj.dob.year - ((today.month, today.day) < (obj.dob.month, obj.dob.day))

