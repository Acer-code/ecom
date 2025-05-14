from django import forms
from core.models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'
        widgets ={
            'Product_Name':forms.TextInput(attrs={'class':'form-control'}),
            'model_no':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'} ),
            'img':forms.FileInput(attrs={'class':'form-control'}),
            'product_catelog':forms.FileInput(attrs={'class':'form-control'}),
            'features':forms.Textarea(attrs={'class':'form-control'}),
        }
# product form end

# blog form start
class BlogForm(forms.ModelForm):

    class Meta:
        model = MyBlog
        fields ='__all__'
        widgets ={
            'blog_title':forms.TextInput(attrs={'class':'form-control'}),
            'blog_desc_1':forms.Textarea(attrs={'class':'form-control'}),
            'blog_desc_2':forms.Textarea(attrs={'class':'form-control'}),
            'blog_desc_3':forms.Textarea(attrs={'class':'form-control'}),
            'blog_desc_4':forms.Textarea(attrs={'class':'form-control'}),
            'blog_desc_5':forms.Textarea(attrs={'class':'form-control'}),
            'img_1':forms.FileInput(attrs={'class':'form-control'}),
            'img_2':forms.FileInput(attrs={'class':'form-control'}),
            'blog_heading_1':forms.TextInput(attrs={'class':'form-control'}),
            'blog_heading_2':forms.TextInput(attrs={'class':'form-control'}),
            'blog_heading_3':forms.TextInput(attrs={'class':'form-control'}),
            'blog_heading_4':forms.TextInput(attrs={'class':'form-control'}),
            'blog_conclusion_h':forms.TextInput(attrs={'class':'form-control'}),
            'blog_desc_conc':forms.Textarea(attrs={'class':'form-control'}),
        }

# blog form end


# Request a call
class RequestCallForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    time = forms.CharField(max_length=50)

# contact us form

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Full Name','class':'form-control'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'Email ','class':'form-control'})
    )
    subject = forms.CharField(
        max_length=200, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'subject','class':'form-control'})
    )
    message = forms.CharField(
        required=True, 
        widget=forms.Textarea(attrs={'placeholder': 'message','class':'form-control'})
    )


class ProductSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False, label='Search')