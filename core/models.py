from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from cloudinary.models import CloudinaryField
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_list", kwargs={"subcategory_name": self.name})
    
class Product(models.Model):
    Product_Name=models.CharField(max_length=100)
    model_no=models.CharField(max_length=100,default="")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products", default="")
    features =models.TextField(help_text="Enter each feature on a new line.",blank=False,null=True)
    # img = models.ImageField(upload_to='images/')
    img = CloudinaryField('product-images/')
    product_catelog = CloudinaryField('product-catalogue/',blank=True,null=True)
    # product_catelog = models.FileField(upload_to='catelogs/',blank=True,null=True)
    def __str__(self):
      return self.Product_Name
    
    def image(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="50" height="50" />')
        return "No Image"

    image.allow_tags = True

# product model end

 # blog model start
class MyBlog(models.Model):
    blog_title=models.CharField(max_length=500)
    blog_desc_1 = models.TextField()
    blog_heading_1=models.CharField(max_length=500,blank=True,null=True)
    blog_desc_2 = models.TextField(blank=True,null=True)
    blog_heading_2=models.CharField(max_length=500,blank=True,null=True)
    blog_desc_3 = models.TextField(blank=True,null=True)

    blog_heading_3=models.CharField(max_length=500,blank=True,null=True)
    blog_desc_4 = models.TextField(blank=True,null=True)
    blog_heading_4=models.CharField(max_length=500,blank=True,null=True)
    blog_desc_5 = models.TextField(blank=True,null=True)
    blog_conclusion_h=models.CharField(max_length=500,blank=True,null=True)
    blog_desc_conc = models.TextField(blank=True,null=True)
   
    img_1 = models.ImageField(upload_to='blog/')
    img_2 = models.ImageField(upload_to='blog/',blank=True,null=True)
    blog_post_date =models.DateField(auto_now_add=True,null=True)
    def __str__(self):
      return self.blog_title
    
    def image(self):
        if self.img_1:
            return mark_safe(f'<img src="{self.img_1.url}" height="50" />')
        return "No Image"

    image.allow_tags = True
 # blog model end  

# Event model start
class Event(models.Model):
    event_name = models.CharField(max_length=300)
    event_date = models.DateField(auto_now_add=False)
    event_img = models.ImageField(upload_to='events/')

    def __str__(self):
        return self.event_name
    
    def image(self):
        if self.event_img:
            return mark_safe(f'<img src="{self.event_img.url}" height="50" />')
        return "No Image"

    image.allow_tags = True
# Event model end