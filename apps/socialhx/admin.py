from django.contrib import admin
from .models import SocialHx

# Register your models here.
@admin.register(SocialHx)
class SocialHxAdmin(admin.ModelAdmin):
  list_display = ['patient','living','working','smoking','drinking','children','family']

  def patient(self,obj):
    return obj.pid