from django.db import models

class Category (models.Model):
    id = models.AutoField (primary_key=True)
    name = models.CharField (max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'
    
class Product (models.Model):
    id = models.AutoField (primary_key= True)
    product_name = models.CharField (max_length=255)
    description = models.TextField(null=True)
    images = models.ImageField(upload_to="product/")
    category_id = models.ForeignKey(Category, null=False ,on_delete=models.CASCADE)