from django.urls import path
from . import views

urlpatterns = [
    path('past/', views.PastOrdersView.as_view(), name='past-orders'),
    path('new/', views.CreateOrderView.as_view(), name='create-order'),
]