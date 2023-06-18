from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=20)
    product_class = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f'Product: {self.product_id} - {self.product_name} - {self.product_class} - {self.price}'


class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=40)
    contact_data = models.CharField(max_length=70)
    user_basket = models.CharField(max_length=150)

    def __str__(self):
        return f'User: {self.user_id} - {self.user_name} - {self.contact_data} - {self.user_basket}'
