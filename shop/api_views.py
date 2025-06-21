from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Товар, Производитель, Категория, Материал, Покупатель
from .serializers import (
    ТоварSerializer, ПроизводительSerializer, КатегорияSerializer, 
    МатериалSerializer, ПокупательSerializer
)
from django.contrib.auth.models import User
from .serializers import UserSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешает чтение всем, но изменение только админам.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.is_superuser

class ТоварViewSet(viewsets.ModelViewSet):
    queryset = Товар.objects.all()
    serializer_class = ТоварSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    @action(detail=False, methods=['get'])
    def галстуки(self, request):
        """Получить только галстуки"""
        товары = Товар.objects.filter(тип='tie')
        serializer = self.get_serializer(товары, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def бабочки(self, request):
        """Получить только бабочки"""
        товары = Товар.objects.filter(тип='bowtie')
        serializer = self.get_serializer(товары, many=True)
        return Response(serializer.data)

class ПроизводительViewSet(viewsets.ModelViewSet):
    queryset = Производитель.objects.all()
    serializer_class = ПроизводительSerializer
    permission_classes = [IsAdminOrReadOnly]

class КатегорияViewSet(viewsets.ModelViewSet):
    queryset = Категория.objects.all()
    serializer_class = КатегорияSerializer
    permission_classes = [IsAdminOrReadOnly]

class МатериалViewSet(viewsets.ModelViewSet):
    queryset = Материал.objects.all()
    serializer_class = МатериалSerializer
    permission_classes = [IsAdminOrReadOnly]

class ПокупательViewSet(viewsets.ModelViewSet):
    queryset = Покупатель.objects.all()
    serializer_class = ПокупательSerializer
    permission_classes = [permissions.IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser] 