from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Производитель(models.Model):
    название = models.CharField(max_length=100)
    страна = models.CharField(max_length=100)
    сайт = models.URLField(blank=True)

    def __str__(self):
        return self.название

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Категория(models.Model):
    название = models.CharField(max_length=100)

    def __str__(self):
        return self.название

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Материал(models.Model):
    название = models.CharField(max_length=100)
    описание = models.TextField()
    экологичный = models.BooleanField(default=False)

    def __str__(self):
        return self.название

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

class Товар(models.Model):
    название = models.CharField(max_length=200)
    описание = models.TextField()
    цена = models.DecimalField(max_digits=10, decimal_places=2)
    изображение = models.ImageField(upload_to='товары/', blank=True, null=True)
    тип = models.CharField(max_length=50)
    производитель = models.ForeignKey(Производитель, on_delete=models.CASCADE)
    категория = models.ForeignKey(Категория, on_delete=models.CASCADE)
    материалы = models.ManyToManyField(Материал, through='МатериалТовара')

    def __str__(self):
        return self.название

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class МатериалТовара(models.Model):
    товар = models.ForeignKey(Товар, on_delete=models.CASCADE)
    материал = models.ForeignKey(Материал, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Материал товара'
        verbose_name_plural = 'Материалы товаров'

class Склад(models.Model):
    товар = models.ForeignKey(Товар, on_delete=models.CASCADE)
    размер = models.CharField(max_length=50)
    цвет = models.CharField(max_length=50)
    количество = models.IntegerField()
    поставщик = models.ForeignKey('Поставщик', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.товар.название} - {self.размер} - {self.цвет}"

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'

class Поставщик(models.Model):
    название = models.CharField(max_length=100)
    контактное_лицо = models.CharField(max_length=100)
    телефон = models.CharField(max_length=20)

    def __str__(self):
        return self.название

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class Покупатель(models.Model):
    пользователь = models.OneToOneField(User, on_delete=models.CASCADE)
    телефон = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.пользователь.first_name} {self.пользователь.last_name}"

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

class СпособДоставки(models.Model):
    название = models.CharField(max_length=100)
    стоимость = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.название

    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'

class Заказ(models.Model):
    покупатель = models.ForeignKey(Покупатель, on_delete=models.CASCADE)
    дата_заказа = models.DateTimeField(auto_now_add=True)
    общая_сумма = models.DecimalField(max_digits=10, decimal_places=2)
    способ_доставки = models.ForeignKey(СпособДоставки, on_delete=models.CASCADE)
    адрес_доставки = models.ForeignKey('АдресДоставки', on_delete=models.CASCADE)

    def __str__(self):
        return f"Заказ #{self.id} от {self.дата_заказа}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ЭлементЗаказа(models.Model):
    заказ = models.ForeignKey(Заказ, on_delete=models.CASCADE)
    товар = models.ForeignKey(Товар, on_delete=models.CASCADE)
    количество = models.IntegerField()

    def __str__(self):
        return f"{self.товар.название} - {self.количество} шт."

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

class Отзыв(models.Model):
    товар = models.ForeignKey(Товар, on_delete=models.CASCADE)
    покупатель = models.ForeignKey(Покупатель, on_delete=models.CASCADE)
    оценка = models.IntegerField()
    комментарий = models.TextField(blank=True)
    дата = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв на {self.товар.название} от {self.покупатель}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Скидка(models.Model):
    товар = models.ForeignKey(Товар, on_delete=models.CASCADE, null=True, blank=True)
    категория = models.ForeignKey(Категория, on_delete=models.CASCADE, null=True, blank=True)
    процент = models.IntegerField()

    def __str__(self):
        if self.товар:
            return f"Скидка {self.процент}% на {self.товар.название}"
        return f"Скидка {self.процент}% на категорию {self.категория.название}"

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

class Оплата(models.Model):
    заказ = models.ForeignKey(Заказ, on_delete=models.CASCADE)
    способ = models.CharField(max_length=50)
    сумма = models.DecimalField(max_digits=10, decimal_places=2)
    дата = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Оплата заказа #{self.заказ.id}"

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

class АдресДоставки(models.Model):
    покупатель = models.ForeignKey(Покупатель, on_delete=models.CASCADE)
    страна = models.CharField(max_length=100)
    город = models.CharField(max_length=100)
    улица = models.CharField(max_length=200)
    дом = models.CharField(max_length=20)
    квартира = models.CharField(max_length=20, blank=True)
    почтовый_индекс = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.страна}, {self.город}, {self.улица}, {self.дом}"

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'
