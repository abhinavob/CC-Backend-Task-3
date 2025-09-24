from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ItemListView.as_view(), name='list-items'),
]