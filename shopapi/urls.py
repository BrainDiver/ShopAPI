from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('', RedirectView.as_view(url= '/shop/', permanent = True)),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
