from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'products'

urlpatterns = [
    path('list/', views.product_list, name='list'),
    path('about/', views.about_page, name='about-page'),
    path('detail/<int:product_id>/', views.product_detail, name='detail'),
    path('create/', views.create_product, name='create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)