from django.db import models
from service.models import Subservice
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
from django.conf import settings



class Order(models.Model):
    STATE = (
        ('PENDING', 'PENDING'),
        ('INPROGRESS', 'INPROGRESS'),
        ('COMPLETED', 'COMPLETED'),
        ('REJECTED' , 'REJECTED'),
        ('CANCELLED', 'CANCELLED'),
    )
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    subservice = models.ManyToManyField(Subservice, blank=True)
    state = models.CharField(max_length=20, choices=STATE, default='PENDING')
    scheduled = models.DateTimeField(blank=True, null=True,default=timezone.now)
    location = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(default=0.0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = ShortUUIDField(primary_key=True, length=6, max_length=6, blank=False, editable=False)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.id + ' ' + self.state + ' ' + str(self.price)

