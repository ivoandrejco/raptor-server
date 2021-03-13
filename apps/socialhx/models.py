
from django.db import models
from django.contrib.auth.models import User

from patients.models import Patient

template = """
lives {{living}}, children: {{children}}, {{working}}, smoking: {{smoking}}, alcohol: {{drinking}}, family hx: {{family}}, {{#if other}}other: {{other}}{{/if}}
"""
# Create your models here.
class SocialHx(models.Model):
  pid             = models.OneToOneField(Patient,on_delete=models.CASCADE,primary_key=True, verbose_name="Patient")
  living          = models.CharField(max_length=255,null=True,blank=True, verbose_name="Living Arrangements")
  working         = models.CharField(max_length=255,null=True,blank=True, verbose_name="Working Arrangements")
  smoking         = models.CharField(max_length=255,null=True,blank=True, verbose_name="Smoking")
  drinking        = models.CharField(max_length=255,null=True,blank=True, verbose_name="Drinking")
  children        = models.CharField(max_length=255,null=True,blank=True, verbose_name="Children")
  family          = models.CharField(max_length=255,null=True,blank=True, verbose_name="Family")
  template        = models.TextField(default=template)
  template_value  = models.TextField()
  created_by      = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="socialhx_created_by")

  class Meta:
    verbose_name_plural = "Social Histories"

  def get_absolute_url(self):
    return reverse('socialhx-view', args=[str(self.id)])

  def __str__(self):
    return f'{self.rendered}'  