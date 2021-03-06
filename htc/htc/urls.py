"""htc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from .views import home, about
from users.views import login, register, logout
from dashboard.views import dashboard, offer, request_ride, rent, contract, offer_details, contract_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),

    # Users
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout, name="logout"),

    # Dashboard
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/offer', offer, name="offer"),
    path('dashboard/request', request_ride, name="request"),
    path('dashboard/rent', rent, name="rent"),
    path('dashboard/contract', contract, name="contract"),
    path('dashboard/rent/<str:offer_name>', offer_details, name="offer_details"),
    path('dashboard/contract/<str:contract_name>', contract_details, name="contract_details"),
]
