from django.contrib import admin
from .models import Comorbidity

# Register your models here.
@admin.register(Comorbidity)
class ComorbidityAdmin(admin.ModelAdmin):
  list_display = ['patient','name','comment']

  def patient(self,obj):
    return obj.pid