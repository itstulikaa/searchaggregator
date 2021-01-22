from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    offer_price = models.CharField(max_length=30)
    actual_price = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

