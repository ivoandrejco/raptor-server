from django.contrib import admin

# Register your models here.
from .models import Claim, ClaimPaid

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display    = ['patient_name','code','amount','billed_on','billed_by']
    list_filter     = ["billed_on","code"]
    search_fields   = ["lname","month","billed_on"]

    def patient_name(self,obj):
        return f'{obj.fname} {obj.lname}'

@admin.register(ClaimPaid)
class ClaimPaidAdmin(admin.ModelAdmin):
    list_display = ['patient_name','code','amount','billed_on','billed_by']
    list_filter     = ("billed_on","code",)
    search_fields   = ("lname","billed_on",)

    def patient_name(self,obj):
        return f'{obj.fname} {obj.lname}'

