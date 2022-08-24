from django.urls import path
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from gui.views import HomeView, ServiceView, ContactView, SuccessView

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [
    path('', HomeView.as_view(), name='gui_home'),
    path('contact/', ContactView.as_view(), name='gui_contact'),   # url on browser, view code, html name
    path('success/' , SuccessView.as_view(), name='gui_success'),
    path('services/' , ServiceView.as_view(), name='gui_services')
]

