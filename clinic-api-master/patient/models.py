from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15, blank=True, null=False)
    medical_operation_date = models.DateField()
    doctor = models.CharField(max_length=100)
    number_of_days = models.IntegerField()
    regiment = models.ForeignKey('Regiment', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.ForeignKey("City", on_delete=models.SET_NULL, blank=True, null=True)
    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)
    disease = models.ForeignKey("Disease", on_delete=models.SET_NULL, blank=True, null=True)
    other_diseases = models.ManyToManyField("Disease", blank=True, related_name="other_diseases")
    img_1 = models.FileField(upload_to='images/',default='images/subservice/default.svg', blank=True, null=True)
    img_2 = models.FileField(upload_to='images/',default='images/subservice/default.svg', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return  self.name + ' ' + self.phone 


class Regiment(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    days = models.ManyToManyField("Day", blank=True)

    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name + ' ' + self.id

class Day(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)

    # class Meta:
    #     ordering = ['-created_at']

    def __str__(self):
        return self.name


class Presence(models.Model):

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.patient.id
    
class Disease(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = ShortUUIDField(primary_key=True, length=11, max_length=11,blank=False, editable=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
