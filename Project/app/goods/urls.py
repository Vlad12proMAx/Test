from goods import views
from django.urls import path

app_name = 'goods'

urlpatterns = [
    path('serch/',views.catalog,name = 'serch'),
    path('<slug:name_slug>/',views.catalog,name = 'index'),
    path('product/<slug:product_slug>/',views. product ,name = 'prod')

]