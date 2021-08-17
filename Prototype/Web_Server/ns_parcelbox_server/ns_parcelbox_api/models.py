from django.db import models

# model creation

class Temperature(models.Model):
    temp = models.Field()
    date_created = models.DateTimeField(
    verbose_name="TimeGenerated", auto_now_add=True)

    def __str__(self):
        d = f"{self.temp}c | Date: {self.date_created.strftime('%h %d %Y %H:%M')}"
        return d

class Humidity(models.Model):
    humidity_level = models.Field()
    date_created = models.DateTimeField(
    verbose_name="TimeGenerated", auto_now_add=True)

    def __str__(self):
        d = f"{self.humidity_level}% | Date: {self.date_created.strftime('%h %d %Y %H:%M')}"
        return d

class Motion(models.Model):
    motion = models.BooleanField(default=False)
    date_created = models.DateTimeField(
    verbose_name="TimeGenerated", auto_now_add=True)

    def __str__(self):
        if bool(self.motion) == True:
            d = f"Motion in front of your parcelbox! At {self.date_created.strftime('%h %d %Y %H:%M')}"
        else:
            d = f"No motion detected. Last checked {self.date_created.strftime('%h %d %Y %H:%M')}"
        return d
