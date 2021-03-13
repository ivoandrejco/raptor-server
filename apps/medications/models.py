import uuid
from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

# Create your models here.
class Medication(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pid         = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="medications",verbose_name="Patient")
    name        = models.CharField(max_length=50)
    dose        = models.CharField(max_length=50, blank=True, null=True)
    frequency   = models.CharField(max_length=50, blank=True, null=True)
    comment     = models.TextField(blank=True,null=True)
    ceased      = models.BooleanField(default=False)
    ceased_on   = models.DateField(blank=True,null=True)
    reviewed_on = models.DateField()
    created_on  = models.DateField()
    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="medications_created_by")

    class Meta:
        verbose_name_plural = "Medications"
        ordering            = ['-name']
        unique_together     = ['pid','name','created_on']

    def get_absolute_url(self):
        return reverse('medication-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.name}'

class Allergy(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pid         = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="allergies", verbose_name="Patient")
    drug        = models.CharField(max_length=50)
    reaction    = models.CharField(max_length=200,blank=True,null=True)
    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="allergies_created_by")

    class Meta:
        verbose_name_plural = "Allergies"
        ordering            = ['-drug']
        unique_together     = ['pid','drug']

    def get_absolute_url(self):
        return reverse('allergy-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.drug} - {self.reaction}'