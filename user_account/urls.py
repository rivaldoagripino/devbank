from django.urls import path
from .views import AddMoneyView, RemoveMoneyView, ExtractView


urlpatterns = [
    path('transactions/add/', AddMoneyView.as_view(), name='transactions'),
    path('transactions/remove/', RemoveMoneyView.as_view(), name='transactions'),
    path('extract/', ExtractView.as_view(), name='extract'),
    
]
