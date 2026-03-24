from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('update/<str:pk>/', views.update_page, name = 'update'),
    path('delete/<str:pk>/', views.delete_page, name = 'delete')
]