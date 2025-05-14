import re
from django.conf import settings
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from core.forms import *
from core.models import *
from .models import Product, Category
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.template.loader import render_to_string
from django.db.models import Q

# Create your views here.


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    events = Event.objects.all()
    return render(request,'core/index.html',{'products':products,'categories':categories,'events':events,'title':'Acer Biomedicals | Hospital Equipment Manufacturer'})

def about(request):
    categories = Category.objects.all()
    return render(request,'core/about.html',{'categories':categories,'title':'Acer Biomedicals | About'})

def certification(request):
    categories = Category.objects.all()
    return render(request,'core/certification.html',{'categories':categories,'title':'Acer Biomedical | Certification'})

def base(request):
    categories = Category.objects.prefetch_related("subcategories").all()
    return {"categories": categories}  

    
# add product start
def add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
       form = ProductForm(request.POST, request.FILES) 
       if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('/')
       else:
           messages.error(request, 'PLEASE CHECK THE DETAILS.')
           messages.info(request,'PRODUCT IS NOT  ADDED...........')
    #    return redirect('/')
    else:
        form = ProductForm()
    return render(request,'core/products/add_product.html',{'form':form,'categories':categories,'title':'Acer Biomedical | Add Product'})

# add product end
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    categories=Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_desc', product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'core/products/edit_product.html', {'form': form, 'product': product,'categories':categories,'titile':'Acer Biomedical | Edit Product'})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        # print("product deleted")
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('all_products')  # Redirect to product list after deletion

    return render(request, 'core/products/product_detail.html', {'product': product,'categories':categories})



# add blog start
def add_blog(request):
    categories = Category.objects.all()
    if request.method == 'POST':
       form = BlogForm(request.POST, request.FILES) 
       if form.is_valid():
            form.save()
            messages.success(request, 'Blog added successfully!')
            return redirect('blog_index')
       else:
           messages.error(request, 'PLEASE CHECK THE FORM.')
           messages.info(request,'Blog IS NOT  ADDED...........')
    #    return redirect('/')
    else:
        form = BlogForm()
    return render(request,'core/blog/add_blog.html',{'form':form,'categories':categories,'title':'Acer Biomedical | Add Blog'})
# add blog end
def edit_blog(request, id):
    blog = get_object_or_404(MyBlog, id=id)
    categories=Category.objects.all()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'blog edited successfully!')
            return redirect('blog', blog.id)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'core/blog/edit_blog.html', {'form': form, 'blog': blog,'categories':categories})

def delete_blog(request, id):
    blog = get_object_or_404(MyBlog, id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        # print("product deleted")
        blog.delete()
        messages.success(request, 'blog deleted successfully!')
        return redirect('blog_index')  # Redirect to product list after deletion

    return render(request, 'core/blog/blog.html', {'blog': blog,'categories':categories})

def main_blog(request):
    blogs = MyBlog.objects.all().order_by('-blog_post_date')
    categories = Category.objects.all()
     # Set up pagination
    paginator = Paginator(blogs, 9) 
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)

    # return render(request, 'blog_index.html', {'page_obj': page_obj})
    return render(request,'core/blog/main-blog.html',{'blogs':blogs,'page_obj': page_obj,'categories':categories,'title':'Acer Biomedicals | Blog'})

def blog_single(request,pk):
    blog = MyBlog.objects.get(pk=pk)
    blogs = MyBlog.objects.all().order_by('-blog_post_date')
    categories = Category.objects.all()
    return render(request,'core/blog/blog-single.html',{'blog':blog,'blogs':blogs,'categories':categories,'title':'Acer Biomedicals | Blog Detail'})

def product_list(request, subcategory_name):
    
    subcategory = SubCategory.objects.get(name=subcategory_name)
    products = Product.objects.filter(subcategory=subcategory)
    category = subcategory.category
    return render(request, "core/products/products.html", {"subcategory": subcategory,"category":category,"products": products,'title':'Acer Biomedicals | Products'})

# product description start
def product_desc(request, pk):
    product = Product.objects.get(pk=pk)
    subcategories = SubCategory.objects.all()
    subcategory = product.subcategory
    


    return render(request, 'core/products/product-detail.html', {
        'product': product,
        'subcategory': subcategory,
        'subcategories': subcategories,'title':'Acer Biomedicals | Product Detail'
    })
# end



def contact_us(request):
    categories = Category.objects.all()
    return render(request, 'core/contact.html', {'categories':categories,'title':'Acer Biomedicals | Contact Us'})




def product_search(request):
    query = request.GET.get('query', '').strip()
    categories = Category.objects.all()
    
    # Initialize an empty queryset to avoid loading all products when no query is provided
    products = Product.objects.none()

    if query:
        products = Product.objects.filter(
            Q(Product_Name__icontains=query) |  
            Q(model_no__icontains=query) 
        )

    return render(request, 'core/products/products.html', {
        'query': query,
        'products': products,
        'categories': categories
    })

