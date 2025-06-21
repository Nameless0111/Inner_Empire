from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.профиль, name='profile'),
    path('api-docs/', views.api_docs, name='api_docs'),
    path('products/<str:product_type>/', views.product_list, name='product_list'),
    path('products/<str:product_type>/create/', views.product_create, name='product_create'),
    path('products/<str:product_type>/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<str:product_type>/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
] 