from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
