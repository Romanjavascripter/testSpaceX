from django.core.management.base import BaseCommand
from go.models import MenuItem, Advantage, HeroContent

class Command(BaseCommand):
    help = 'Load initial data for menu and advantages'

    def handle(self, *args, **kwargs):
        # Меню
        menu_items = [
            {'title': 'Главная', 'url': '#', 'order': 1},
            {'title': 'Технологии', 'url': '#', 'order': 2},
            {'title': 'График полетов', 'url': '#', 'order': 3},
            {'title': 'Гарантии', 'url': '#', 'order': 4},
            {'title': 'О компании', 'url': '#', 'order': 5},
            {'title': 'Контакты', 'url': '#', 'order': 6},
        ]
        
        for item in menu_items:
            MenuItem.objects.get_or_create(title=item['title'], defaults=item)
        
        # Преимущества
        advantages = [
            {'title': 'МЫ', 'value': '1', 'description': 'на рынке', 'order': 1},
            {'title': 'ГАРАНТИРУЕМ', 'value': '50%', 'description': 'безопасность', 'order': 2},
            {'title': 'ПУТЕШЕСТВИЕ', 'value': '597', 'description': 'дней', 'order': 3},
            {'title': 'КАЛЕНДАРИК ЗА', 'value': '2001г.', 'description': 'в подарок', 'order': 4},
        ]
        
        for adv in advantages:
            Advantage.objects.get_or_create(title=adv['title'], defaults=adv)
        
        # Hero контент
        HeroContent.objects.get_or_create(
            pk=1,
            defaults={
                'main_title': 'ПУТЕШЕСТВИЕ',
                'title_highlight': 'ВИЕ',
                'subtitle': 'на красную планету',
                'button_text': 'Начать путешествие',
                'button_url': '#'
            }
        )
        
        self.stdout.write(self.style.SUCCESS('Initial data loaded successfully!'))