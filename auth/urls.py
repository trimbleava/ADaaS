from django.urls import path

from auth.views import SignupView


urlpatterns = [
    # url on browser, view code, html name
    path('signup/', SignupView.as_view(), name='auth_signup'),
]