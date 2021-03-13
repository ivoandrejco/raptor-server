from django.contrib import admin
from .models import Doctor,ProviderNumber

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','specialty','phone','email']

    def doctor_name(self,obj):
        return f'{obj.first_name} {obj.last_name}'

@admin.register(ProviderNumber)
class ProviderNumberAdmin(admin.ModelAdmin):
    list_display = ['id','number','doctor','practice']
