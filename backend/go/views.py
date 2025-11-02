from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem, Advantage, HeroContent
from .serializers import MenuItemSerializer, AdvantageSerializer, HeroContentSerializer


@api_view(['GET'])
def menu_items(request):
    """API для получения пунктов меню"""
    items = MenuItem.objects.filter(is_active=True)
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def advantages(request):
    """API для получения блоков преимуществ"""
    items = Advantage.objects.filter(is_active=True)
    serializer = AdvantageSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def hero_content(request):
    """API для получения контента главного экрана"""
    content, created = HeroContent.objects.get_or_create(pk=1)
    serializer = HeroContentSerializer(content)
    return Response(serializer.data)