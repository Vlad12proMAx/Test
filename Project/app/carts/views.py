from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from carts.models import Cart
from goods.models import Product
from carts.utils import get_user_carts
# Create your views here.

def cart_add(request,product_slug):
    product = Product.objects.get(slug=product_slug) #Объект продукта который нужно добавить
    
    if request.user.is_authenticated: #Проверка на авторизацию пользователя.
        carts = Cart.objects.filter(user=request.user, product=product) #данные корзины и пользователя 

        if carts.exists(): #проверка на сущестоввание продукта в корзине
            cart = carts.first() # Продукт
            if cart:
                cart.quantity += 1
                cart.save() #добавили и сохранили 
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1) #Создается корзину с  1-им продуктом 

    return redirect(request.META['HTTP_REFERER'])#возвращает пользователя на ту страницу на которой он был (HTTP_REFERER-отвечает с какой стр мы попали)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": cart}, request)

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)



def cart_remove(request):
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)