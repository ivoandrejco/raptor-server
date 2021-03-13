import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from patients.models import Patient
from templates.models import Investigation as TemplateInvestigation, Issue as TemplateIssue
from doctors.models import ProviderNumber
from diagnoses.models import Diagnosis



# Create your models here.
class Consultation(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pid         = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="consultation_pid", verbose_name="Patient")
    code        = models.IntegerField()
    provider    = models.ForeignKey(ProviderNumber,on_delete=models.CASCADE,related_name="provider_consultations",verbose_name="Provider")
    weight      = models.FloatField(blank=True,null=True)
    height      = models.FloatField(blank=True,null=True)
    pulse       = models.CharField(max_length=50,blank=True,null=True)
    BP          = models.CharField(max_length=8,blank=True,null=True,verbose_name="Blood Pressure")
    presentation = models.TextField(blank=True,null=True)
    examination = models.TextField(blank=True,null=True)
    conclusion  = models.TextField(blank=True,null=True)
    presentation  = models.TextField(blank=True,null=True)
    plan          = models.TextField(blank=True,null=True)
    created_on  = models.DateTimeField()
    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="consultation_created_by")

    class Meta:
        verbose_name_plural = "Consultations"
        ordering            = ['-created_on']
        unique_together     = ['pid','code','created_on']

    def get_absolute_url(self):
        return reverse('consultation-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.pid}: {self.code} {self.created_on}'

class Issue(models.Model):
    id             = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cid            = models.ForeignKey(Consultation,on_delete=models.CASCADE,related_name="issues", verbose_name="Consultation")
    tid            = models.ForeignKey(TemplateIssue,on_delete=models.SET_NULL,related_name="template_issue", null=True, blank=True, verbose_name="Template")
    title          = models.CharField(max_length=50)
    comment        = models.TextField(blank=True,null=True)
    json           = models.JSONField(null=True,blank=True)
    tags           = models.TextField(blank=True,null=True)
    value          = models.TextField(blank=True,null=True)
    presentation   = models.TextField(null=True,blank=True)
    conclusion     = models.TextField(null=True,blank=True)
    updated_on     = models.DateField()
    created_on     = models.DateField()
    created_by     = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="issue_created_by")

    class Meta:
        verbose_name_plural = "Issues"
        ordering            = ['-updated_on','-created_on']
        unique_together     = ['cid','title','created_on']

    def get_absolute_url(self):
        return reverse('issue-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.title}'

class Investigation(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    iid             = models.ForeignKey(Issue,on_delete=models.CASCADE,related_name="investigations", verbose_name="Issue")
    tid             = models.ForeignKey(TemplateInvestigation,on_delete=models.SET_NULL,related_name="template_investigation", null=True, blank=True, verbose_name="Template")
    title           = models.CharField(max_length=50)
    json            = models.JSONField(null=True,blank=True)
    value           = models.TextField(null=True,blank=True)
    comment         = models.TextField(null=True,blank=True)
    updated_on      = models.DateField()
    created_on      = models.DateField()
    created_by      = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="investigation_created_by")

    class Meta:
        verbose_name_plural = "Investigations"
        ordering            = ['-title']
        unique_together     = ['iid','title','created_on']

    def get_absolute_url(self):
        return reverse('investigation-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.title}'

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
