from django import forms
from .models import Товар
 
class ТоварForm(forms.ModelForm):
    class Meta:
        model = Товар
        fields = ['название', 'описание', 'цена', 'изображение', 'тип', 'производитель', 'категория', 'материалы'] 