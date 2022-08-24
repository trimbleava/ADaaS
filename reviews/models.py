from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Company(models.Model):
    # This is the entity receiving and processing the ad leads.
    # We assume, this entity has at least a customized web page tailored to receive
    # the response from an ad and process the ad contents.
    name = models.CharField(max_length=255)
    url = models.TextField()

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    class Meta:  
        db_table = "category"
  
    def __str__(self):
        return self.name



class Product(models.Model):
    # the offering product or service - to think more
    name = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='products')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = "product"
        ordering = ['-created']

    def __str__(self):
        return self.name


class ProductSite(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    productsize = models.ForeignKey(ProductSize, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = "product_site"

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = "comment"
        
    def __str__(self):
        return self.title


# 
# With Django the validation is performed partially on the form, and partially on the model instance. 
# With Django Rest Framework the validation is performed entirely on the serializer class.
#
class CustomerReportRecord(models.Model):
    time_raised = models.DateTimeField(default=timezone.now, editable=False)
    reference = models.CharField(unique=True, max_length=20)
    description = models.TextField()