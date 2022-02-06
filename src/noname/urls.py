"""noname URL Configuration
miejsce na komentarz
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from blog.views import (
    blog_post_create_view,
)
from .views import (
    home_page,
    about_page,
    contact_page)

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('about/', about_page),
    path('contact/', contact_page),
    path('blog-new/', blog_post_create_view),
    path('blog/', include('blog.urls')),
]


if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)