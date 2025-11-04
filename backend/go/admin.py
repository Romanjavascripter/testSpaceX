from django.contrib import admin
from .models import MenuItem, Advantage, HeroContent

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'description', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')


@admin.register(HeroContent)
class HeroContentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Заголовок', {
            'fields': ('main_title', 'title_highlight', 'subtitle')
        }),
        ('Кнопка', {
            'fields': ('button_text', 'button_url')
        }),
        ('Фон', {
            'fields': ('background_image',)
        }),
    )