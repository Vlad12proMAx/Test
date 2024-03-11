from carts import views
from django.urls import path

app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:product_slug>/',views.cart_add,name = 'cart_add'),
    path('cart_change',views.cart_change,name = 'cart_change'),
    path('cart_remove',views. cart_remove ,name = 'cart_remove')

]