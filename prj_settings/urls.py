"""ADaaS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4.0+.
# The easiest fix is to replace url() with re_path(). re_path uses regexes like url, 
# so you only have to update the import and replace url with re_path.

from django.urls import include, path, re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.views.defaults import permission_denied, page_not_found, server_error

#
from rest_framework.routers import DefaultRouter

from reviews.views import ProductViewSet


""" from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) """

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Apps
    path(r'', include('gui.urls')),

    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^', include(router.urls)),
# ]

"""
if settings.DEBUG:

    # Serve media files through Django.
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    # Show error pages during development
    urlpatterns += [
        re_path(r'^403/$', permission_denied),
        re_path(r'^404/$', page_not_found),
        re_path(r'^500/$', server_error)
    ]
"""
