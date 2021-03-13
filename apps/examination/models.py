import uuid
from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

# Create your models here.
class Examination(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pid           = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="examinations",verbose_name="Patient")
    weight        = models.FloatField(blank=True,null=True)
    height        = models.FloatField(blank=True,null=True)
    pulse         = models.IntegerField(blank=True,null=True)
    pulse_desc    = models.CharField(max_length=8,blank=True,null=True,verbose_name="Pulse Description")
    BP            = models.CharField(max_length=8,blank=True,null=True,verbose_name="Blood Pressure")
    temp          = models.FloatField(blank=True,null=True)
    sats          = models.IntegerField(blank=True,null=True)
    findings      = models.TextField(blank=True,null=True,verbose_name="Findings")
    collected_on  = models.DateField()
    created_by    = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="examination_created_by")

    class Meta:
        verbose_name_plural = "Examinations"
        ordering            = ['-collected_on']
        unique_together     = ['pid','collected_on']

    def get_absolute_url(self):
        return reverse('examination-view', args=[str(self.id)])    

    def __str__(self):
        return f'Examination: {self.pid} - {self.collected_on}'
