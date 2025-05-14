from django.contrib import admin

# Register your models here.
from core.models import Category, Product, MyBlog, SubCategory, Event

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_Name', 'image')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'image')

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'image')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(MyBlog, BlogAdmin)
admin.site.register(SubCategory)
admin.site.register(Event, EventAdmin)
# Customizing the Django Admin Panel
admin.site.site_header = "Acer Biomedicals"
admin.site.site_title = "Acer Admin Panel"
admin.site.index_title = "Welcome to Acer Biomedicals Dashboard"