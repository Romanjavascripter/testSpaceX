from django.db import models
from django.core.validators import MinValueValidator

class MenuItem(models.Model):
    """Модель для пунктов главного меню"""
    title = models.CharField(max_length=100, verbose_name="Название")
    url = models.CharField(max_length=200, verbose_name="URL", blank=True, null=True)
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    
    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ['order']
    
    def __str__(self):
        return self.title


class Advantage(models.Model):
    """Модель для блока преимуществ"""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    value = models.CharField(max_length=100, verbose_name="Значение (число или текст)")
    description = models.CharField(max_length=200, verbose_name="Описание")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    
    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} - {self.value}"


class HeroContent(models.Model):
    """Модель для главного заголовка и описания"""
    main_title = models.CharField(max_length=200, default="ПУТЕШЕСТВИЕ", verbose_name="Главный заголовок")
    title_highlight = models.CharField(max_length=50, default="ВИЕ", verbose_name="Выделенная часть заголовка")
    subtitle = models.CharField(max_length=200, default="на красную планету", verbose_name="Подзаголовок")
    button_text = models.CharField(max_length=100, default="Начать путешествие", verbose_name="Текст кнопки")
    button_url = models.CharField(max_length=200, default="#", verbose_name="URL кнопки")
    
    class Meta:
        verbose_name = "Контент главного экрана"
        verbose_name_plural = "Контент главного экрана"
    
    def __str__(self):
        return "Контент главного экрана"
    
    def save(self, *args, **kwargs):
        # Ограничиваем количество записей до одной
        self.pk = 1
        super().save(*args, **kwargs)
