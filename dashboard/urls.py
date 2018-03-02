"""PMDesk_web URL Configuration

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
from django.urls import path
from dashboard import views

urlpatterns = [
    path('acquisition/place-impressions/', views.place_impressions, name='place_impressions'),
    path('acquisition/place-quality/', views.place_quality, name='place_quality'),
    path('activation', views.activation, name='activation'),
    path('retention', views.retention, name='retention'),
    path('revenue', views.revenue, name='revenue'),
    path('refer/initiative', views.initiative_refer, name='initiative_refer'),
    path('refer/passive', views.passive_refer, name='passive_refer'),
]
