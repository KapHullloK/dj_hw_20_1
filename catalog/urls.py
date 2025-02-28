from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home_menu'),
    path('more/<int:pk>', ProductDetailView.as_view(), name='about_prod'),
    path('catalog/', ContactTemplateView.as_view(), name='contacts'),
]
