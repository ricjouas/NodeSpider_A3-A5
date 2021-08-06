from django.db import models

# model creation

class Temperature(models.Model):
    temp = models.IntegerField()
    date_created = models.DateTimeField(
    verbose_name="TimeGenerated", auto_now_add=True)

    def __str__(self):
        d = f"Temp: {self.temp} | Date: {self.date_created}"
        return d

class Humidity(models.Model):
    humidity_level = models.IntegerField()
    date_created = models.DateTimeField(
    verbose_name="TimeGenerated", auto_now_add=True)

    def __str__(self):
        d = f"Humidity: {self.humidity_level} | Date: {self.date_created}"
        return d

class Motion(models.Model):
    motion = models.BooleanField(default=False)
    date_created = models.DateTimeField(
    verbose_name="TimeGenerated", auto_now_add=True)

    def __str__(self):
        if bool(self.motion) == True:
            d = f"No motion detected. Last checked {self.date_created}"
        else:
            d = f"Motion in front of your parcelbox! At {self.date_created}"
        return d