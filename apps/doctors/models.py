import uuid
from django.db import models

from practices.models import Practice

# Create your models here.
class Doctor(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name      = models.CharField(max_length=50,verbose_name="First Name")
    last_name       = models.CharField(max_length=50,verbose_name="Last Name")
    email           = models.EmailField(verbose_name="Email",null=True, blank=True)
    phone           = models.CharField(max_length=20,verbose_name="Phone", null=True, blank=True)
    specialty       = models.CharField(max_length=30,verbose_name="Specialty")

    class Meta:
        ordering    = ['last_name','first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.specialty}'


class ProviderNumber(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    number          = models.CharField(max_length=20,verbose_name="Provider Number")
    doctor          = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    practice        = models.ForeignKey(Practice,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.number} - {self.doctor} - {self.practice}'
