from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm
from oscar.apps.catalogue.models import *
from django import forms

class ProductForm(CoreProductForm):    
    class Meta(CoreProductForm.Meta):
    	model = Product
    	widgets ={'structure': forms.Select}