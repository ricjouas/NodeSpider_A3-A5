from django.contrib import admin
from .models import Temperature
from .models import Humidity
from .models import Motion

# model registration

admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Motion)

