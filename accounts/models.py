from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=300, blank=True, null=True)
    profile_img = models.ImageField(upload_to='image/', default='image/user.png')
    financial_products = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    desire_amount_saving = models.IntegerField(blank=True, null=True)
    desire_amount_deposit = models.IntegerField(blank=True, null=True)
    deposit_period = models.IntegerField(blank=True, null=True)
    saving_period = models.IntegerField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)