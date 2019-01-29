from django import forms

from .models import Product


class ProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    summary = forms.CharField()
    featured = forms.BooleanField()
