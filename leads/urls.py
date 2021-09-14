from django.contrib import admin
from django.urls import path
from .views import LeadViewSet, BrokerageAPIView

urlpatterns = [
    path('leads', LeadViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('leads/<str:pk>', LeadViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('broker', BrokerageAPIView.as_view()),
]
