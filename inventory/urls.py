from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ItemListView.as_view(), name='list-items'),
    path('new/', views.ItemCreateView.as_view(), name='create-item'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update-item'),
    path('restock/<int:pk>/', views.ItemRestockView.as_view(), name='restock-item'),
    path('orders/', views.OrderListView.as_view(), name='display-orders'),
    path('revenue/', views.OrderRevenueView.as_view(), name='total-revenue')
]