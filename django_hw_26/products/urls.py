from django.urls import path
from .views import add_product, product_details, add_category, \
    category_details, edit_product

urlpatterns = [
    path("/add", add_product, name="add_product"),
    path("/<int:id>", product_details, name="product_details"),
    path("/edit/<int:id>", edit_product, name="edit_product"),
    path("/category/add", add_category, name="add_category"),
    path("/category/details", category_details, name="category_details")
]
