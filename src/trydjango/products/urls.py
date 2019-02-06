from django.urls import path
from .views import *

urlpatterns = [
    path('create/', product_create_view),
    path('<int:my_id>/', dynamic_lookup_view, name="product-details"),
    path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list'),

]
