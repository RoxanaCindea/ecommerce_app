from django.urls import path
from cart import views

#comm 

urlpatterns = [
    path('', views.cart_list, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add-cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove-cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove-cart-item'),

    path('checkout/', views.checkout, name='checkout'),
]
