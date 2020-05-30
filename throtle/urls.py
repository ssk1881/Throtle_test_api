from django.contrib import admin
from django.urls import path, re_path, include

from throtle import views
from rest_framework import routers
from . import views
app_name = "throtle"

router = routers.DefaultRouter()
router.register(r'request', views.ResponseViewer)

urlpatterns = [
    # /home/
    re_path(r'^home', views.home, name='home'),

    # /home/
    re_path(r'^processing', views.processing, name='processing'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
