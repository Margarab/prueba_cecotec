"""bernini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from products import models as product_models
from orders.admin import admin_site

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product_models.Product
        fields = ('id', 'ean', 'name', 'description', 'price')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = product_models.Product.objects.all()
    serializer_class = ProductSerializer


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('',admin_site.urls),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls))

]
