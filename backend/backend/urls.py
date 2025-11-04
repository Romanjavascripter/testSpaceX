from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from pathlib import Path
from django.http import HttpResponse

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('go.urls')),
]

# Для раздачи медиа файлов в development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Простая раздача media для продакшена на Render (без отдельного CDN)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

# Проверка существования build файла
build_index_path = BASE_DIR.parent / 'frontend' / 'frontend' / 'build' / 'index.html'

if build_index_path.exists():
    # React Router - должен быть последним, НО исключаем api, admin, static, media
    urlpatterns += [
        re_path(r'^(?!api|admin|static|media).*', TemplateView.as_view(template_name='index.html')),
    ]
else:
    # Fallback для development, если build еще не создан
    if settings.DEBUG:
        urlpatterns += [
            path('', lambda request: HttpResponse('React build not found. Run: cd frontend/frontend && npm run build', content_type='text/plain')),
        ]