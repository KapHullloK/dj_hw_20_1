from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, ProductCreateView, ProductUpdateView, \
    VersionCreateView, VersionUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home_menu'),
    path('more/<int:pk>', ProductDetailView.as_view(), name='about_prod'),
    path('create/', ProductCreateView.as_view(), name='create_prod'),
    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_prod'),
    path('update_version/<int:pk>', VersionUpdateView.as_view(), name='update_version'),
    path('catalog/', ContactTemplateView.as_view(), name='contacts'),
]
