from django.urls import path
from core import views

urlpatterns = [


    path('',views.index,name='index'),
    path('add-product',views.add_product,name='add_product'),
    path('product/edit/<int:id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('certification',views.certification,name='certification'),
    # path('products',views.fetch_product_cate,name='fetch_product_cate'),
    path('product-description/<pk>',views.product_desc, name = "product_desc"),

    path('about',views.about,name='about'),
    path('add-blog',views.add_blog,name='add_blog'),
    
    path('blog/edit/<int:id>/', views.edit_blog, name='edit_blog'),
    path('blog/delete/<int:id>/', views.delete_blog, name='delete_blog'),
    path('blog/main-blog',views.main_blog,name='main_blog'),
    path('blog/blog-single/<pk>',views.blog_single,name='blog_single'),
    
    path('contact/', views.contact_us, name='contact_us'),
     path('products/<str:subcategory_name>/', views.product_list, name='product_list'),
    
     path('search/', views.product_search, name='product_search'),
]
