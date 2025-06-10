from django.db import models

# Create your models here.

class Product(models.Model):
    TIE = 'tie'
    BOWTIE = 'bowtie'
    PRODUCT_TYPE_CHOICES = [
        (TIE, 'Галстук'),
        (BOWTIE, 'Бабочка'),
    ]
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES, verbose_name='Тип')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return self.name
