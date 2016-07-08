from __future__ import unicode_literals
from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator


Rating = [(i,i) for i in range(6)]


class Category(models.Model):
    name_category = models.CharField(max_length=200, unique=True)
    description_category = models.TextField(blank=True,null=True)
    banner_category = models.ImageField(upload_to='images/banner_categories',blank=True,null=True)
    sort_order_category = models.IntegerField(default=0)
    status_category = models.BooleanField()
    slug_category = AutoSlugField(populate_from='name_category', always_update=True, unique=True)
    created_at_category = models.DateTimeField(auto_now_add=True)
    updated_at_category = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_category

class Subcategory(models.Model):
    name_subcategory = models.CharField(max_length=200, unique=True)
    category_subcategory = models.ForeignKey(Category)
    icon_subcategory = models.ImageField(upload_to='images/icons_subcategories',blank=True,null=True)
    sort_order_subcategory = models.IntegerField(default=0)
    status_subcategory = models.BooleanField()
    slug_subcategory = AutoSlugField(populate_from='name_subcategory', always_update=True, unique=True)
    created_at_subcategory = models.DateTimeField(auto_now_add=True)
    updated_at_subcategory = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_subcategory


class Brand(models.Model):
    name_brand = models.CharField(max_length=200, unique=True)
    banner_brand = models.ImageField(upload_to='images/banner_brands',blank=True,null=True)
    created_at_brand = models.DateTimeField(auto_now_add=True)
    updated_at_brand = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_brand


class Image(models.Model):
    name_image = models.CharField(max_length=200, unique=True)
    sort_order_image = models.IntegerField(default=0)
    image_image = models.ImageField(upload_to='images/products',blank=True,null=True)
    created_at_image = models.DateTimeField(auto_now_add=True)
    updated_at_image = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_image


class Product(models.Model):
    name_product = models.CharField(max_length=100, unique=True)
    brand_product = models.ForeignKey(Brand)
    extract_product = models.CharField(max_length=100)
    description_product = models.TextField()    
    slug_product = AutoSlugField(populate_from='name_product', always_update=True, unique=True)
    sku_product = models.CharField(max_length=100, unique=True)
    price_product = models.DecimalField(max_digits=11, decimal_places=2)
    rating_product = models.IntegerField(choices=Rating)
    subcategory_product = models.ForeignKey(Subcategory)
    status_product = models.BooleanField()
    created_at_product = models.DateTimeField(auto_now_add=True)
    updated_at_product = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_product

class Product_Image(models.Model):
    product_pi= models.ForeignKey(Product)
    image_pi = models.ForeignKey(Image)
    created_at_pi = models.DateTimeField(auto_now_add=True)
    updated_at_pi = models.DateTimeField(auto_now=True)


class Slider(models.Model):
    title_slider = models.CharField(max_length=100, unique=True)
    image_slider = models.ImageField(upload_to='images/sliders',blank=True,null=True)
    description_slider = models.TextField()
    sort_order_slider = models.IntegerField(default=0)
    status_slider = models.BooleanField()
    created_at_slider = models.DateTimeField(auto_now_add=True)
    updated_at_slider = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_slider


