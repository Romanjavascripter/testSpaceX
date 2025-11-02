from django.urls import path
from .views import menu_items, advantages, hero_content

urlpatterns = [
    path('menu/', menu_items, name='menu_items'),
    path('advantages/', advantages, name='advantages'),
    path('hero/', hero_content, name='hero_content'),
]