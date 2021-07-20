from django.db import models

# Create your models here.
class engine(models.Model):
    sap = models.CharField(max_length=200)
    ledger = models.CharField(max_length=200)
    manufacture = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    vehicle_type = models.CharField(max_length=200)
    base_km = models.CharField(max_length=200)
    rto = models.CharField(max_length=200)
    model_year = models.CharField(max_length=200)
    chassis = models.CharField(max_length=200)
    fuel_type = models.CharField(max_length=200)
    old_vehicle = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)