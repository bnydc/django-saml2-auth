from django.urls import include, re_path
from . import views

app_name = 'django_saml2_auth'

urlpatterns = [
    re_path(r'^acs/$', views.acs, name="acs"),
    re_path(r'^welcome/$', views.welcome, name="welcome"),
    re_path(r'^denied/$', views.denied, name="denied"),
]
