from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('laptops/', views.LaptopListView.as_view(), name='laptops'),
    path('laptop/<int:pk>', views.LaptopDetailView.as_view(), name='laptop-detail'),
]
