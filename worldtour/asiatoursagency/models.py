from django.db import models

class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return (f'ID : {self.id} \n From {self.origin_country} to {self.destination_country} for {self.number_of_nights} nights at {self.price}')