import uuid
from math import pow, sqrt

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from patients.models import Patient
from doctors.models import ProviderNumber



# Create your models here.
class Consultation(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient     = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="consultation_pid", verbose_name="Patient")
    code        = models.IntegerField()
    provider    = models.ForeignKey(ProviderNumber,on_delete=models.CASCADE,related_name="provider_consultations",verbose_name="Provider")
    history     = models.TextField()
    impression  = models.TextField(blank=True,null=True)
    plan        = models.TextField()
    created_on  = models.DateTimeField()
    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="consultation_created_by")

    class Meta:
        verbose_name_plural = "Consultations"
        ordering            = ['-created_on']
        unique_together     = ['patient','code','created_on']

    def get_absolute_url(self):
        return reverse('consultation-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.patient}: {self.code} {self.created_on}'


LETTER_CHOICES = (
  ('Pending','Pending'),
  ('Completed','Completed'),
)

# Create your models here.
class Letter(models.Model):
  id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  cid         = models.ForeignKey(Consultation,on_delete=models.CASCADE,related_name="letters",verbose_name="Consultation")
  status      = models.CharField(max_length=10, verbose_name="Status",default="Pending",choices=LETTER_CHOICES)
  title       = models.CharField(max_length=100)
  content     = models.TextField()
  updated_on  = models.DateField()
  created_on  = models.DateField()
  created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="letters_created_by")

  class Meta:
      verbose_name_plural = "Letters"
      ordering            = ['-created_on']
      unique_together     = ['cid','created_on']

  def get_absolute_url(self):
      return reverse('letter-view', args=[str(self.id)])    

  def __str__(self):
       return f'Letter: {self.cid} - {self.created_on} {self.title}'







######################################
#       EXAMINATION MODEL 
######################################

def is_number(n):
    return isinstance(n,(int,float)) and n > 0

def check_params(func):
    def wrapper(h,w):
        if is_number(h) and is_number(w):
            return func(h,w)
        return None
    return wrapper


def IBW(h,g):
    if is_number(h) is False:
        return None

    if g=='Male':
        return 50 + 0.9 * (h-152)
    elif g=='Female':
        return 45.5 + 0.9 * (h-152)

    return None

def ABW(h,w,g):
    if is_number(h) and is_number(w):
        return IBW(h,g) + 0.4 * (w-IBW(h,g))
    return None

@check_params
def BMI(h,w):
    return round(w/pow(h/100,2),1)

@check_params
def BSA_D(h,w):
    return round(0.007184 * pow(h,0.725) * pow(w,0.425),2)

@check_params
def BSA_M(h,w):
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
    sats_desc     = models.CharField(max_length=30,blank=True,null=True,verbose_name="Saturation Description")
    findings      = models.TextField(blank=True,null=True,verbose_name="Findings")
    collected_on  = models.DateField()
    updated_on    = models.DateField()
    created_by    = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="examination_created_by")

    def save(self,*args,**kwargs):
        h           = self.height
        w           = self.weight
        g           = self.consultation.patient.gender

        self.BSA_D  = BSA_D(h,w)
        self.BSA_M  = BSA_M(h,w)
        self.BMI    = BMI(h,w)
        self.IBW    = IBW(h,g)
        self.ABW    = ABW(h,w,g)
        super().save(*args,**kwargs)

    def update(self,*args,**kwargs):
        h           = self.height
        w           = self.weight
        g           = self.consultation.patient.gender

        self.BSA_D  = BSA_D(h,w)
        self.BSA_M  = BSA_M(h,w)
        self.BMI    = BMI(h,w)
        self.IBW    = IBW(h,g)
        self.ABW    = ABW(h,w,g)

        super(Examination,self).update(*args,**kwargs)

    class Meta:
        verbose_name_plural = "Examinations"
        ordering            = ['-collected_on']
        unique_together     = ['consultation','collected_on']

    def get_absolute_url(self):
        return reverse('examination-view', args=[str(self.id)])    

    def __str__(self):
        return f'Examination: {self.consultation.patient} - {self.collected_on}'
