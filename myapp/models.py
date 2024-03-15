from django.db import models

from users.models import User


class Season(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='seasons/')

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='collection/', blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='category/', blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ceil = models.IntegerField(default=0, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.CharField(unique=True, max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    product_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.name} -- Quantity: {self.quantity}"

    @property
    def total_price(self):
        return self.price*self.quantity
