from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    ТоварViewSet, ПроизводительViewSet, КатегорияViewSet, 
    МатериалViewSet, ПокупательViewSet, UserViewSet
)

router = DefaultRouter()
router.register(r'товары', ТоварViewSet)
router.register(r'производители', ПроизводительViewSet)
router.register(r'категории', КатегорияViewSet)
router.register(r'материалы', МатериалViewSet)
router.register(r'покупатели', ПокупательViewSet)
router.register(r'пользователи', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 