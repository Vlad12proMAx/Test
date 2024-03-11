from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product')
    #Еслии пользователь зарег то фун возвращает корзину со всеми данными
    
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')
#Проверкана сессию если нет то создается новая и возвращает корзины с этой сессией