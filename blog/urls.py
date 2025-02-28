from django.urls import path

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('more/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='blog-update'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='blog-delete'),
]
