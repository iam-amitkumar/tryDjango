from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

from .forms import ProductForm

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
	my_context = {
		"name" 		: "Amit",
		"technology": "DevOps",
		"company"	: "BridgeLabz",
		"contact"	: 9876543210,
		# "list1"		: [123, 456, 789]
		"list1"		: [('0123'), 456, 789, 12.5, 345]
	}

	return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def product_detail_view(request):
	obj = Product.objects.get(id=5)
	context = {
		'object': obj
	}
	return render(request, "products/detail.html", context)


def product_create_view(request):
	my_form = ProductForm()
	if request.method == "POST":
		my_form = ProductForm(request.POST)
		if my_form.is_valid():
			# print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
			my_form = ProductForm()
		else:
			print(my_form.errors)
	context = {
		"form": my_form
	}
	return render(request, "products/product_create.html", context)
