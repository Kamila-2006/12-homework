from django.urls import path
from . import views



app_name = 'products'

urlpatterns = [
    path('list/', views.product_list, name='list'),
    path('about/', views.about_page, name='about-page'),
    path('detail/<int:product_id>/', views.product_detail, name='detail'),
    path('create/', views.create_product, name='create'),
]

