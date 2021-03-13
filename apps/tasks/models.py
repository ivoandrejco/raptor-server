import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from patients.models import Patient

STATUS_CHOICES = (
  ('Pending','Pending'),
  ('Completed','Completed'),
)
# Create your models here.
class Task(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pid         = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="task_pid",verbose_name="Patient")
    name        = models.CharField(max_length=200)
    status      = models.CharField(max_length=9,choices=STATUS_CHOICES,default='Pending')
    updated_on  = models.DateField()
    created_on  = models.DateField()
    created_by  = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name="tasks_created_by")

    class Meta:
        ordering= ['-updated_on','-created_on']
        unique_together=['pid','name','created_on']

    def get_absolute_url(self):
        return reverse('task-view', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'