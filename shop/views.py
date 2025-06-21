from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Товар, Покупатель
from .forms import ТоварForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def home(request):
    return render(request, 'shop/home.html')

def product_list(request, product_type):
    товары = Товар.objects.filter(тип=product_type)
    return render(request, 'shop/product_list.html', {
        'товары': товары,
        'product_type': product_type
    })

def is_admin(user):
    return user.is_superuser or user.is_staff

def is_buyer(user):
    return not is_admin(user)

# Регистрация
from django import forms
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = False
            user.is_superuser = False
            user.save()
            Покупатель.objects.create(пользователь=user)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})

# Вход
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})

# Выход
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# Профиль пользователя
@login_required
def профиль(request):
    users = None
    if is_admin(request.user):
        users = User.objects.all()
    return render(request, 'shop/profile.html', {'users': users})

# Ограничение доступа к CRUD товарам только для админа
@user_passes_test(is_admin)
def product_create(request, product_type):
    if request.method == 'POST':
        form = ТоварForm(request.POST, request.FILES)
        if form.is_valid():
            товар = form.save(commit=False)
            товар.тип = product_type
            товар.save()
            form.save_m2m()
            return redirect('product_list', product_type=product_type)
    else:
        form = ТоварForm(initial={'тип': product_type})
    return render(request, 'shop/product_form.html', {'form': form, 'product_type': product_type})

@user_passes_test(is_admin)
def product_update(request, product_type, pk):
    товар = get_object_or_404(Товар, pk=pk, тип=product_type)
    if request.method == 'POST':
        form = ТоварForm(request.POST, request.FILES, instance=товар)
        if form.is_valid():
            form.save()
            return redirect('product_list', product_type=product_type)
    else:
        form = ТоварForm(instance=товар)
    return render(request, 'shop/product_form.html', {'form': form, 'product_type': product_type, 'edit': True})

@user_passes_test(is_admin)
def product_delete(request, product_type, pk):
    товар = get_object_or_404(Товар, pk=pk, тип=product_type)
    if request.method == 'POST':
        товар.delete()
        return redirect('product_list', product_type=product_type)
    return render(request, 'shop/product_confirm_delete.html', {'object': товар, 'product_type': product_type})

def каталог(request):
    return HttpResponse('Каталог (заглушка)')

def детали_товара(request, товар_id):
    return HttpResponse(f'Детали товара {товар_id} (заглушка)')

def корзина(request):
    return HttpResponse('Корзина (заглушка)')

def оформление_заказа(request):
    return HttpResponse('Оформление заказа (заглушка)')

def заказы(request):
    return HttpResponse('Заказы (заглушка)')

def детали_заказа(request, заказ_id):
    return HttpResponse(f'Детали заказа {заказ_id} (заглушка)')

def добавить_отзыв(request, товар_id):
    return HttpResponse(f'Добавить отзыв к товару {товар_id} (заглушка)')

@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.all()
    return render(request, 'shop/user_list.html', {'users': users})

@user_passes_test(is_admin)
def user_edit(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data.get('password'):
                user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_list')
    else:
        form = RegisterForm(instance=user)
    return render(request, 'shop/user_edit.html', {'form': form, 'user_obj': user})

def api_docs(request):
    return render(request, 'shop/api_docs.html')
