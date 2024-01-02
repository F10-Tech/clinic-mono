from django.db import models
from service.models import Subservice
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
from django.conf import settings
from patient.models import Patient



class Order(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.FloatField(default=0)
    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.id 

