from django.db import models

MEMBERSHIP_BRONZE = 'B'
MEMBERSHIP_SILVER = 'S'
MEMBERSHIP_GOLD = 'G'

MEMBERSHIP_CHOICES = [
  (MEMBERSHIP_BRONZE, 'Bronze'),
  (MEMBERSHIP_SILVER, 'Silver'),
  (MEMBERSHIP_GOLD, 'Gold'),
]

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.IntegerField()
  last_update = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
  firsrt_nme = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=255)
  birth_date = models.DateField(null=True)
  membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)