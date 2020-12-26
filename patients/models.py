from django.db import models
import uuid


# Create your models here.

class Patient(models.Model):
    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname   = models.CharField(max_length=50,help_text="First Name")
    lname   = models.CharField(max_length=50,help_text="Last Name")
    dob     = models.DateField()
    gender  = models.CharField(max_length=6,help_text="Gender", choices=[("Male","Male"),("Female","Female")])

    class Meta:
        ordering= ['-lname']

    def get_absolute_url(self):
        return reverse('patient-view', args=[str(self.id)])

    def __str__(self):
        return f'{self.fname} {self.lname}'
