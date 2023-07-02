
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pereval import views

router = routers.SimpleRouter()
router.register(r'pereval\api', views.PerevalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]