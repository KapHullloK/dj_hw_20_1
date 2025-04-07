from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Exists, OuterRef
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        active_versions = Version.objects.filter(product=OuterRef('pk'), active=True)
        return Product.objects.filter(Exists(active_versions))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        product_ids = [product.id for product in context['products']]
        active_versions = {}

        for version in Version.objects.filter(product_id__in=product_ids, active=True):
            active_versions[version.product.pk] = version

        for product in context['products']:
            product.version = active_versions[product.pk]
            product.description = product.description[:100]
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'prod'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'prod'
    success_url = reverse_lazy('catalog:home_menu')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'prod'
    success_url = reverse_lazy('catalog:home_menu')


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home_menu')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home_menu')
