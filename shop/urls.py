from django.urls import path
from shop import views

app_name = 'shop'
urlpatterns = [
    path('detail/<int:product_id>', views.detail, name='detail'),
    path('bill', views.show_bill, name='bill'),
    path('order', views.order_status, name='order_status')
]
