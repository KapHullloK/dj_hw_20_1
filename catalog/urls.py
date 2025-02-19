from django.urls import path
from catalog.views import index, about_prod

app_name = 'catalog'

urlpatterns = [
    path('', index, name='home_menu'),
    path('more/<int:pk>', about_prod, name='about_prod'),
]
