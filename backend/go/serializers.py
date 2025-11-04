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
    background_image_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroContent
        fields = ['main_title', 'title_highlight', 'subtitle', 'button_text', 'button_url', 'background_image_url']

    def get_background_image_url(self, obj):
        request = self.context.get('request')
        if obj.background_image:
            url = obj.background_image.url
            return request.build_absolute_uri(url) if request else url
        return None