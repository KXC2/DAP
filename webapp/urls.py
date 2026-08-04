from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name='register'),
    path('view_journal/', views.view_journal, name='view_journal'),
    path('deposit/', views.deposit, name='deposit'),
    path('StandardDeposit/', views.StandardDeposit, name='StandardDeposit'),
    path('DialAndPay/', views.DialAndPay, name='DialAndPay'),
    path('check_number/', views.check_number, name='check_number'),
    path ('add/', views.add_journal_entry, name = 'add_journal'),
]