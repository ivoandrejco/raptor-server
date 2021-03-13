import uuid
from django.db import models

# Create your models here.
class Practice(models.Model):
    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label   = models.CharField(max_length=50,verbose_name="Label")
    name    = models.CharField(max_length=100, verbose_name="Full Name")
    address = models.CharField(max_length=100, verbose_name="Address", null=True, blank=True)
    phone   = models.CharField(max_length=20, verbose_name="Phone", null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.label}'
