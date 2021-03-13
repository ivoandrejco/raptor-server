import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

  
# Create your models here.
class Template(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kind          = models.CharField(max_length=13,choices=(("Issue","Issue"),("Investigation","Investigation")))    
    title         = models.CharField(max_length=50)
    json          = models.JSONField()
    tags          = models.TextField(blank=True,null=True)
    presentation  = models.TextField(blank=True,null=True)
    hints         = models.TextField(blank=True,null=True)
    conclusion    = models.TextField(blank=True,null=True)
    comment       = models.TextField(blank=True,null=True)
    created_by    = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="template_created_by")

    class Meta:
        verbose_name_plural = "Templates"
        ordering            = ['-title']
        unique_together     = ['title','kind','json']

    def get_absolute_url(self):
        return reverse('template-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.kind} - {self.title}'

 
# Create your models here.
class Investigation(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title         = models.CharField(max_length=50)
    slug          = models.TextField(null=True,blank=True)
    json          = models.JSONField()
    tags          = models.TextField(blank=True,null=True)
    comment       = models.TextField(blank=True,null=True)
    created_by    = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="investigation_templates")

    class Meta:
        verbose_name_plural = "Investigations"
        ordering            = ['-title']
        unique_together     = ['title','json']

    def get_absolute_url(self):
        return reverse('template-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.title}'


class Issue(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title         = models.CharField(max_length=50)
    slug          = models.TextField(null=True,blank=True)
    json          = models.JSONField()
    tags          = models.TextField(blank=True,null=True)
    differential  = models.TextField(blank=True,null=True)
    presentation  = models.TextField(blank=True,null=True)
    conclusion    = models.TextField(blank=True,null=True)
    created_by    = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="issue_templates")

    class Meta:
        verbose_name_plural = "Issues"
        ordering            = ['-title']
        unique_together     = ['title','json']

    def get_absolute_url(self):
        return reverse('template-issue-view', args=[str(self.id)])    

    def __str__(self):
        return f'{self.title}'