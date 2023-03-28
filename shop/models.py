from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 20)
    price = models.FloatField(max_length= 20)
    category = models.ForeignKey('Category', on_delete= models.CASCADE, related_name= 'category_products')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length =20)
    
    def __str__(self):
        return self.name

class Costumer(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    adress = models.TextField(max_length = 20)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name 
