import uuid
from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from templates.models import Investigation as TemplateInvestigation

# Create your models here.
class Diagnosis(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient     = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="diagnoses",verbose_name="Patient")
    kind        = models.CharField(max_length=10, verbose_name="Type",choices=(("Issue","Issue"),("Diagnosis","Diagnosis")))
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_on  = models.DateField()
    updated_on  = models.DateField()
    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="diagnoses_created_by")

    class Meta:
        verbose_name_plural = "Diagnoses"
        ordering            = ['-title']
        unique_together     = ['patient','title']

    def get_absolute_url(self):
        return reverse('diagnosis-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.patient} - {self.title}'


class Investigation(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diagnosis       = models.ForeignKey(Diagnosis,on_delete=models.CASCADE,related_name="investigations", verbose_name="Diagnosis")
    template        = models.ForeignKey(TemplateInvestigation,on_delete=models.SET_NULL,related_name="template_investigation", null=True, blank=True, verbose_name="Template")
    json            = models.JSONField(null=True,blank=True)
    value           = models.TextField(null=True,blank=True)
    comment         = models.TextField(null=True,blank=True)
    updated_on      = models.DateField()
    created_on      = models.DateField()
    created_by      = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="investigation_created_by")

    class Meta:
        verbose_name_plural = "Investigations"
        ordering            = ['-updated_on','created_on']
        unique_together     = ['diagnosis','template']

    def get_absolute_url(self):
        return reverse('investigation-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.template.title}'

