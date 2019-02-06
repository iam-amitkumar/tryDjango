from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

from .forms import ProductForm

from django.http import Http404, HttpResponseRedirect


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


def product_create_view(request):
	my_form = ProductForm()
	if request.method == "POST":
		my_form = ProductForm(request.POST)
		if my_form.is_valid():
			# print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
			# my_form = ProductForm()  # to reset form after submission of form in database
			return HttpResponseRedirect('../')  # to redirect the page after submit the form to database to a specific location
		else:
			print(my_form.errors)
	context = {
		"form": my_form
	}
	return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, my_id):
	# obj = Product.objects.get(id=my_id)
	# obj = get_object_or_404(Product, id=my_id)
	try:
		obj = Product.objects.get(id=my_id)
	except Product.DoesNotExist:
		raise Http404

	context = {
		'object': obj
	}
	return render(request, "products/detail.html", context)


def product_delete_view(request, my_id):
	# obj = Product.objects.get(id=my_id)
	# obj = get_object_or_404(Product, id=my_id)
	try:
		obj = Product.objects.get(id=my_id)
	except Product.DoesNotExist:
		raise Http404

	# deleting object with confirmation
	if request.method == "POST":
		# confirming delete
		obj.delete()
		# redirecting after object deletion
		return redirect('../../')
	context = {
		'object': obj
	}
	return render(request, "products/product_delete.html", context)


def product_list_view(request):
	queryset = Product.objects.all()  # list all object instances present in the database
	context = {
		"object_list": queryset
	}
	return render(request, "products/product_list.html", context)
