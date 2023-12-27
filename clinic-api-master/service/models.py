from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField

class Service(models.Model):
    name_EN = models.CharField(max_length=50)
    description_EN = models.CharField(max_length=100)
    name_AR = models.CharField(max_length=50, blank=True, null=True)
    description_AR = models.CharField(max_length=100, blank=True, null=True)
    name_FR = models.CharField(max_length=50, blank=True, null=True)
    description_FR = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    image_light = models.FileField(upload_to='images/service/', default='images/subservice/default.svg',  null=True, blank=True)
    image_dark = models.FileField(upload_to='images/service/', default='images/subservice/default.svg',  null=True, blank=True)
    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)




    def __str__(self):
        return self.name_EN


class Subservice(models.Model):
    name_EN = models.CharField(max_length=50, blank=True, null=True)
    description_EN = models.CharField(max_length=100, blank=True, null=True)
    name_AR = models.CharField(max_length=50, blank=True, null=True)
    description_AR = models.CharField(max_length=100, blank=True, null=True)
    name_FR = models.CharField(max_length=50, blank=True, null=True)
    description_FR = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    min_price = models.IntegerField(default=0, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    image_light = models.FileField(upload_to='images/subservice/', default='images/subservice/default.svg', blank=True, null=True)
    image_dark = models.FileField(upload_to='images/subservice/', default='images/subservice/default.svg', blank=True, null=True)
    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)




    def __str__(self):
        return self.id