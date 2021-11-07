from django.db import models

class VehicleProfile(models.Model):
    name = models.CharField('Vehicle model', max_length=10)
    vehicle_image = models.ImageField(upload_to='event_images/')
    vehicle_text = models.CharField(max_length=300)
    mileage_per_day = models.CharField('mileage_per_day', max_length=10)
    mileage_per_year = models.CharField('mileage_per_year', max_length=10)
    number_of_tech_actions = models.CharField('number_of_tech_actions', max_length=10)
    fuel_consumption = models.CharField('fuel_consumption', max_length=10)
    number_of_failures = models.CharField('number_of_failures', max_length=10)

    def __str__(self):
        return self.name
