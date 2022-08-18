from django.urls import path, re_path, include
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView


from gui.views import HomeView, ContactView, SuccessView

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
print("in gui.urls..............")
urlpatterns = [
    path('', HomeView.as_view(), name='gui_home'),
    path('contact/', ContactView.as_view(), name='gui_contact'),   # url on browser, view code, html name
    path('success/' , SuccessView.as_view(), name='gui_success'),

]

