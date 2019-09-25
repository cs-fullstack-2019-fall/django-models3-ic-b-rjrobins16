from django.db import models

# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=50)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    squarefeet = models.DecimalField(max_digits=30, decimal_places=10)

    def __str__(self):
        return self.address
