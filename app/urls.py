from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_now, name='buy_now'),
    path('success/', views.payment_success, name='payment_success'),
    path('failed/', views.payment_failed, name='payment_failed'),
]