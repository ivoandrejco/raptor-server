import uuid
from math import pow, sqrt

from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from consultations.models import Consultation

def BMI(h,w):
    if h==0 or w==0:
        return 0

    return round(w/pow(h/100,2),1)

def IBW(g,h):
    if h==0:
        return 0

    if g=='Male':
        return 50 + 0.9 * (h-152)
    elif g=='Female':
        return 45.5 + 0.9 * (h-152)

    return 0

def ABW(g,h,w):
    return IBW(g,h) + 0.4 * (w-IBW(g,h))

def BSA_D(h,w):
    if h==0 or w==0:
        return 0

    return round(0.007184 * pow(h,0.725) * pow(w,0.425),2)

def BSA_M(h,w):
    if h==0 or w==0:
        return 0

    return round(sqrt(h*w/3600),2)

# Create your models here.
class Examination(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    consultation  = models.ForeignKey(Consultation,on_delete=models.CASCADE,related_name="examinations",verbose_name="Consultation")
    weight        = models.FloatField(blank=True,null=True)
    height        = models.FloatField(blank=True,null=True)
    BMI           = models.FloatField(blank=True,null=True)
    IBW           = models.FloatField(blank=True,null=True,verbose_name='Ideal Body Weight')
    ABW           = models.FloatField(blank=True,null=True,verbose_name='Adjusted Body Weight')
    BSA_D         = models.FloatField(blank=True,null=True,verbose_name='Body Surface Area(Dubois)')
    BSA_M         = models.FloatField(blank=True,null=True,verbose_name='Body Surface Area(Mosteller)')
    pulse         = models.IntegerField(blank=True,null=True)
    pulse_desc    = models.CharField(max_length=8,blank=True,null=True,verbose_name="Pulse Description")
    BP            = models.CharField(max_length=8,blank=True,null=True,verbose_name="Blood Pressure")
    temp          = models.FloatField(blank=True,null=True)
    sats          = models.IntegerField(blank=True,null=True)
    findings      = models.TextField(blank=True,null=True,verbose_name="Findings")
    collected_on  = models.DateField()
    updated_on    = models.DateField()
    created_by    = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="examination_created_by")

    def save(self,*args,**kwargs):
        h           = self.height
        w           = self.weight
        patient     = Patient.objects.get(pk=self.consultation.patient)
        gender      = patient.gender

        self.BSA_D  = BSA_D(h,w)
        self.BSA_M  = BSA_M(h,w)
        self.BMI    = BMI(h,w)
        self.IBW    = IBW(gender,h)
        self.ABW    = ABW(gender,h,w)

        super().save(*args,**kwargs)

    def update(self,*args,**kwargs):
        h           = self.height
        w           = self.weight
        patient     = Patient.objects.get(pk=self.consultation.patient)
        gender      = patient.gender

        self.BSA_D  = BSA_D(h,w)
        self.BSA_M  = BSA_M(h,w)
        self.BMI    = BMI(h,w)
        self.IBW    = IBW(gender,h)
        self.ABW    = ABW(gender,h,w)

        super().update(*args,**kwargs)

    class Meta:
        verbose_name_plural = "Examinations"
        ordering            = ['-collected_on']
        unique_together     = ['consultation','collected_on']

    def get_absolute_url(self):
        return reverse('examination-view', args=[str(self.id)])    

    def __str__(self):
        return f'Examination: {self.consultation.patient} - {self.collected_on}'
