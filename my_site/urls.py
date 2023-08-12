"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from version1.views import *

API_V1 = 'api/v1/'

router = routers.DefaultRouter()
router.register(r'user', UserAPIViewSet)
router.register(r'movie', MovieAPIViewSet)
router.register(r'status_code', StatusCodeAPIViewSet)
router.register(r'feedback', FeedbackAPIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_V1, include(router.urls)),
    path(f'{API_V1}headers', HeadersView.as_view()),
    path(f'{API_V1}ip', IpView.as_view())
]
