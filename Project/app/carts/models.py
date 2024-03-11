from django.db import models
from goods.models import Product

from user.models import User

# Create your models here.


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)#Вычисление общую стоимости всех продуктов
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)#Вычисление общее кол-во всех продуктов
        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects = CartQueryset().as_manager()

    def products_price(self):
        return round(self.product.totol_price() * self.quantity, 2)
    
