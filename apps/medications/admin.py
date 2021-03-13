from django.contrib import admin

# Register your models here.
from .models import Medication, Allergy

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display    = ['patient','name','dose','frequency','ceased','ceased_on','reviewed_on','comment']
    search_fields   = ["patient","name"]

    def patient(self,obj):
        return obj.pid


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
  list_display = ['patient','drug','reaction']

  def patient(self,obj):
    return obj.pid