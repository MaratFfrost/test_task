from django.contrib import admin
from .models import Sensor, Modem, Counter

admin.site.register(Modem)
admin.site.register(Counter)
admin.site.register(Sensor)
