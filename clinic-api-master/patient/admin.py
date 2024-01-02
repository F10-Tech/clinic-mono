from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Regiment)
admin.site.register(Presence)
admin.site.register(Disease)
admin.site.register(Day)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Price)