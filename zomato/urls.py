from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.add_dish_view, name='home'),
    path('add_dish/', views.add_dish_view, name='add_dish'),
    path('display_dishes/', views.display_dishes, name='display_dishes'),
    path('update_dishes/', views.update_availability, name='update_dishes'),
    path('delete_dish/', views.delete_dish, name='delete_dish'),
    path('take_order/', views.take_order_view, name='take_order'),
    path('display_orders/', views.display_orders, name='display_orders'),
    path('update_order_status/', views.update_order_status, name='update_order_status'),




]
#