from django.urls import path

from shop import views

app_name = 'services'


urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_change/', views.cart_change, name='cart_change'),
    path('cart_remove/', views.cart_remove, name='cart_remove'),
    path('create-order/', views.create_order, name='create_order'),
]