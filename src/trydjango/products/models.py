from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	email = models.EmailField(default="example@sample.com")
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10)
	summary = models.TextField(blank=True, null=False)
	featured = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse("product-details", kwargs={"my_id": self.id})  # f"/products/{self.id}/"
		# kwargs is something which we pass to the method present in "views.py"
