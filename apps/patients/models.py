import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname       = models.CharField(max_length=50,verbose_name="First Name")
    lname       = models.CharField(max_length=50,verbose_name="Last Name")
    dob         = models.DateField(blank=True,null=True)
    gender      = models.CharField(max_length=6,help_text="Gender", choices=[("Male","Male"),("Female","Female")])
#    accessed_on = models.DateField()
#    updated_on  = models.DateField()
#    created_on  = models.DateField()
#    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="issue_created_by")

    

    class Meta:
        ordering= ['-lname']
        unique_together=['fname','lname','dob']

    def get_absolute_url(self):
        return reverse('patient-view', args=[str(self.id)])

    def __str__(self):
        return f'{self.fname} {self.lname}'
