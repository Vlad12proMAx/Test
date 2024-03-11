from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length = 50,unique = True,verbose_name = 'Название')
    slug = models.SlugField(max_length = 50,unique = True,blank = True,null = True,verbose_name = 'URL')

    class Meta:
        verbose_name = 'Категорию',
        verbose_name_plural = 'Категории'

    
    def __str__(self):#self-текущий экземпляр объекта
        return self.name
    
    

class Product(models.Model):
    name = models.CharField(max_length = 50,unique = True,verbose_name = 'Название')
    slug = models.SlugField(max_length = 50,unique = True,blank = True,null = True,verbose_name = 'URL')
    description = models.TextField(blank = True,null = True,verbose_name = 'Описание')
    img = models.ImageField(upload_to="Photo",blank = True,null = True ,verbose_name = 'Фото')
    price = models.DecimalField(default = 0.00,max_digits = 7, decimal_places = 2,verbose_name = 'Цена')
    discount = models.DecimalField(default = 0.00,max_digits = 7, decimal_places = 2,verbose_name = 'Скидки')
    quantity = models.PositiveIntegerField(default = 0,verbose_name = 'Количество')
    category = models.ForeignKey(to = Categories, on_delete = models.CASCADE,verbose_name = 'Категория')



    class Meta:
        verbose_name = 'Продукт',
        verbose_name_plural = 'Продукты'

    def __str__(self): #self-текущий экземпляр объекта
        return self.name
    
    def dispaly_id(self):
        return f'{self.id:05}'
    
    def totol_price(self):
        if self.discount:
            return round((self.price-self.price*self.discount/100),2)
        
        return self.price