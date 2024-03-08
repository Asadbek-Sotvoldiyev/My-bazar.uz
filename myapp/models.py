from django.db import models


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

