from django.urls import path
from .views import AddMoneyView, RemoveMoneyView, ExtractView


urlpatterns = [
    path('transactions/add/', AddMoneyView.as_view(), name='transactions'),
    path('transactions/remove/', RemoveMoneyView.as_view(), name='transactions'),
    path('extract/', ExtractView.as_view(), name='extract'),
    path('extract/<str:type>', ExtractView.as_view(), name='extract_with_type'),
    path('extract/<str:initial>&<str:final>/', ExtractView.as_view(), name='extract_with_filter'),
    path('extract/<str:initial>&<str:final>/<str:type>/', ExtractView.as_view(), name='extract_with_filter_type'),
]
