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
from lab import views

urlpatterns = [
    path('market/competitor/', views.market_competitor, name='market_competitor'),
    path('market/ranking/', views.market_ranking, name='market_ranking'),
    path('user/portrait/', views.user_portrait, name='user_portrait'),
    path('user/behavior/', views.user_behavior, name='user_behavior'),
    path('user/group/', views.user_group, name='user_group'),
    path('event/performance/', views.event_performance, name='event_performance'),
    path('event/behavior-path/', views.event_behavior_path, name='event_behavior_path'),
    path('event/relation/', views.event_relation, name='event_relation'),
    path('version/info/', views.version_info, name='version_info'),
    path('version/effect/', views.version_effect, name='version_effect'),
]
