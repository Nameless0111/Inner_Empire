from django.contrib import admin
from .models import Товар, Категория, Производитель, Материал, МатериалТовара, Склад, Поставщик, Покупатель, СпособДоставки, Заказ, ЭлементЗаказа, Отзыв, Скидка, Оплата, АдресДоставки

admin.site.register(Товар)
admin.site.register(Категория)
admin.site.register(Производитель)
admin.site.register(Материал)
admin.site.register(МатериалТовара)
admin.site.register(Склад)
admin.site.register(Поставщик)
admin.site.register(Покупатель)
admin.site.register(СпособДоставки)
admin.site.register(Заказ)
admin.site.register(ЭлементЗаказа)
admin.site.register(Отзыв)
admin.site.register(Скидка)
admin.site.register(Оплата)
admin.site.register(АдресДоставки)