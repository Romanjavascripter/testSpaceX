from rest_framework import serializers
from .models import MenuItem, Advantage, HeroContent


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'url', 'order']


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ['id', 'title', 'value', 'description', 'order']


class HeroContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroContent
        fields = ['main_title', 'title_highlight', 'subtitle', 'button_text', 'button_url']