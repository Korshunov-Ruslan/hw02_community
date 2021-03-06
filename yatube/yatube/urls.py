from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #  регистрация и авторизация
    path('auth/', include('users.urls', namespace='users')),

    #  если нужного шаблона для /auth не нашлось в файле users.urls —
    #  ищем совпадения в файле django.contrib.auth.urls
    path("auth/", include("django.contrib.auth.urls")),

    #  раздел администратора
    path("admin/", admin.site.urls),

    #  обработчик для главной страницы ищем в urls.py приложения posts
    path("", include("posts.urls", namespace="posts_urls")),
    path("about/", include("about.urls", namespace="about"))]
