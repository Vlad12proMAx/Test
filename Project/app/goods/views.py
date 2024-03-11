from django.shortcuts import render
from goods.models import Product
from django.core.paginator import Paginator


def catalog(request,name_slug=None):
    page = request.GET.get('page',1) # Выбор Номера страницы
    on_sale = request.GET.get("on_sale",None) #Скидки
    order_by = request.GET.get("order_by",None)#Категория товаров(дешево-дорого)
    querty = request.GET.get("q",None)#Поиск
    

    if name_slug == 'vse-tovary':
        goods = Product.objects.all() 
    
    elif querty:
        def q_serch(querty):
            if querty.isdigit() and len(querty) <= 5: 
                return Product.objects.filter(id=int(querty))

        goods = q_serch(querty)

    else:
        goods = Product.objects.filter(category__slug = name_slug) 

    if on_sale:
        goods = goods.filter(discount__gt = 0  )  
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)


    paginator = Paginator(goods,2) #Разбиение кол-во объектов товара на странице
    current_page = paginator.page(int(page)) #Доступ к след странице

    context ={
        'title':'Каталог', 
        'goods': current_page,
        'name_cat':name_slug,
        }

    return render(request, 'goods/catalog.html',context)



def product(request,product_slug):

    product = Product.objects.get(slug = product_slug)

    context = {
        'title':'Продукт',
        'product': product
        
        }

    return render(request, 'goods/product.html',context)
