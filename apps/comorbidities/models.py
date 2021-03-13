import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from patients.models import Patient

# Create your models here.
class Comorbidity(models.Model):
  id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  pid         = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="comorbidities",verbose_name="Patient")
  name        = models.CharField(max_length=50)
  comment     = models.CharField(max_length=200,blank=True,null=True)
  created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="comorbidities_created_by")

  class Meta:
    verbose_name_plural = "Comorbidities"
    ordering            = ['-name']
    unique_together     = ['pid','name']

  def get_absolute_url(self):
    return reverse('comorbidity-view', args=[str(self.id)])

  def __str__(self):
    return f'{self.name}'  