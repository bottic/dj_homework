from django.db import models


class Sensor(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
