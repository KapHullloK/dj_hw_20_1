from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        for product in context['products']:
            product.description = product.description[:100]
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'prod'


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
