from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code
from django.shortcuts import reverse

# Create your models here.


class Position(models.Model):
    ''' Position = Product * Quantity.
    It gives us some price.
    Here, foreign key = Product.
    '''
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)
    # if DateTimeField has autonow add = true,
    # the field remains invisible to user.

    def __str__(self):
        return f"id: {self.id}, product:{self.product.name}, quantity:{self.quantity}"

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def get_sales_id(self):
        sale_obj = self.sale_set.first()
        return sale_obj.id

    def get_sales_customer(self):
        sale_obj = self.sale_set.first()
        return sale_obj.customer.name


class Sale(models.Model):
    ''' Sale will consist of multiple positions. 
    Ex - 3 TVs + 4 Keyboards + 2 Laptops = 3 positions to 1 customer = 1 sale
    '''
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"sales for the amount of ${self.total_price}"

    def get_absolute_url(self):
        return reverse('sales:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()

        if self.created is None:
            self.created = timezone.now()

        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()


class CSV(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    csv_file = models.FileField(upload_to='csvs', null=True)
    # activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)