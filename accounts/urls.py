from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='products'),
    path('customers/<str:pk>/', views.customers,name='customers'),
    path('create_order/<str:pk>',views.createOrder,name="create_order"),
    path('update_order/<str:pk_test>/',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>/',views.deleteOrder,name='delete_order'),
]