from django.contrib import admin
from django.urls import path
from fans.views import home, set_settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('set_settings/', set_settings, name='set_settings'),
]