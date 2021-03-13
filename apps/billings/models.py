from django.db import models
from django.contrib.auth.models import User
import uuid

from doctors.models import ProviderNumber

# Create your models here.
class Claim(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname       = models.CharField(max_length=50,verbose_name="First Name")
    lname       = models.CharField(max_length=50,verbose_name="Last Name")
    code        = models.IntegerField()
    amount      = models.FloatField()
    billed_on   = models.DateField()
    billed_by   = models.ForeignKey(ProviderNumber,on_delete=models.CASCADE,related_name="claim_billed_by")
    dob         = models.DateField(null=True,blank=True)
    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="claim_created_by")
    

    class Meta:
        ordering= ['-billed_on']
        unique_together=['fname','lname','billed_on','billed_by']

    def get_absolute_url(self):
        return reverse('billings-claim-view', args=[str(self.id)])

    def __str__(self):
        return f'{self.fname} {self.lname} - {self.billed_on}'


class ClaimPaid(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname       = models.CharField(max_length=50,verbose_name="First Name",help_text="First Name")
    lname       = models.CharField(max_length=50,verbose_name="Last Name",help_text="Last Name")
    code        = models.IntegerField()
    amount      = models.FloatField()
    billed_on   = models.DateField()
    paid_on     = models.DateField()
    billed_by   = models.ForeignKey(ProviderNumber,on_delete=models.CASCADE,related_name="claim_paid_billed_by")
    dob         = models.DateField(null=True,blank=True)
    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="claim_paid_created_by")

    class Meta:
        ordering= ['-billed_on']
        unique_together=['fname','lname','billed_on','billed_by']
        verbose_name_plural='Claims Paid'

    def get_absolute_url(self):
        return reverse('billings-claim-paid-view', args=[str(self.id)])

    def __str__(self):
        return f'{self.fname} {self.lname} {self.billed_on}'


