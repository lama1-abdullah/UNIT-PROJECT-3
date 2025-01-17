from django.urls import path
from . import views

app_name = "products"

urlpatterns = [ 
    path("", views.display_products_view, name="display_products_view"),
    path("add/", views.add_products_view, name="add_products_view"),
    path("not/", views.not_exist_view, name="not_exist_view"),
    path("search/", views.search_results_view, name="search_results_view"),
    path("detail/<product_id>/", views.product_detail_view , name="product_detail_view"),
    path("delete/<product_id>/", views.delete_product_view, name="delete_product_view"),
    path("update/<product_id>/", views.update_product_view, name="update_product_view"),
    path("product/<product>/", views.product_home_view_pro, name="product_home_view_pro"),
]