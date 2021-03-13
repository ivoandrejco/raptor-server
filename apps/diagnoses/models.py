import uuid
from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

# Create your models here.
class Diagnosis(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pid         = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="diagnoses",verbose_name="Patient")
    kind        = models.CharField(max_length=10, verbose_name="Type",choices=(("Issue","Issue"),("Diagnosis","Diagnosis")))
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_on  = models.DateField()
    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="diagnoses_created_by")

    class Meta:
        verbose_name_plural = "Diagnoses"
        ordering            = ['-title']
        unique_together     = ['pid','title']

    def get_absolute_url(self):
        return reverse('diagnosis-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.pid} - {self.title}'
