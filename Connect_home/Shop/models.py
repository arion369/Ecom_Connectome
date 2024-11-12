from django.db import models


# Create your models here.

# category table - cat_id, cat_name, cat_descr,
# product table -  p_id, p_name, cat_id, p_image,p_price, p_Available, P_Date


class Category(models.Model):
    name = models.CharField(max_length=50)  # models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    description = models.TextField()  # TextFiled(Blank=True)
    category_sub = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_On = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Product(models.Model):
    # P_ID = models.IntegerField()
    name = models.CharField(max_length=50)  # models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    description = models.TextField()  # TextFiled(Blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    product_category = models.CharField(max_length=50)
    last_updated_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products')
    product_available = models.BooleanField(default=False)
    product_stock = models.IntegerField()

    def __str__(self):
        return self.name
