from django.conf.urls import include, url
from . import views

app_name = 'KT1'

urlpatterns = [
    url(r'^top$', views.index, name="index"),
    url(r'^ks_admin$',views.ks_admin, name="Ksadmin"),
]