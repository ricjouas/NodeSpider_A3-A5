from django.contrib import admin
from .models import Temperature, Humidity, Motion

# model registration

admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Motion)

