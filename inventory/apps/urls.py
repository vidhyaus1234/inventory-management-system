from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/<int:id>/edit/', views.category_update, name='category_update'),
    path('categories/<int:id>/delete/', views.category_delete, name='category_delete'),

    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:id>/edit/', views.product_update, name='product_update'),
    path('products/<int:id>/delete/', views.product_delete, name='product_delete'),
]