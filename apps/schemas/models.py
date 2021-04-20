import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Schema(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kind          = models.CharField(max_length=30,choices=(("issue","Issue"),("investigation","Investigation")))
    title         = models.CharField(max_length=50)
    ordering      = models.IntegerField(default=0)
    json          = models.JSONField()
    updated_on    = models.DateField()
    created_on    = models.DateField()
    created_by    = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="schema_created_by")

    class Meta:
        verbose_name_plural = "Schemas"
        ordering            = ['ordering']
        unique_together     = ['title','kind']

    def get_absolute_url(self):
        return reverse('schema-view', args=[str(self.id)])

    def __str__(self):
        return f'{self.kind} - {self.title}'

