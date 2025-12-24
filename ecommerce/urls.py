"""
URL configuration for ecommerce project.

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

from authentication.models import Person
from authentication import views as person_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"persons", person_views.PersonViewSet)
router.register(r"memberships", person_views.MembershipViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/auth/", include("authentication.auth.urls")),

    path('admin/', admin.site.urls),
    path('hello/', person_views.hello_view, name='hello'),
]
