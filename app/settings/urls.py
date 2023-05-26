"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import settings.settings

from currency.views import IndexView

schema_view = get_schema_view(
   openapi.Info(
      title="Tracky API",
      default_version='v1',
      description="Open Tracky API",
      terms_of_service="https://www.tracky.io/terms/",
      contact=openapi.Contact(email="tracky@tracky.io"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('auth/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', IndexView.as_view(), name='homepage'),

    path('currency/', include('currency.urls')),
    path('api/currency/', include('currency.api.urls')),
    path('api/', include('account.api.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.settings.base.MEDIA_URL, document_root=settings.settings.base.MEDIA_ROOT)
