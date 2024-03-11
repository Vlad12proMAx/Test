from user import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', views.logout, name = 'logout'),
    path('user_carts/', views.user_carts, name = 'user_carts'),
]