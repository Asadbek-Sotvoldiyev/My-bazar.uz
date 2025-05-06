from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('favorite/', include('favorite.urls', namespace='favorite')),
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('myapp.urls')),
    path('users/', include('users.urls', namespace='users')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
