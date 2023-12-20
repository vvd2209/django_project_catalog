from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Contacts, Product, Version


# Create your views here.

# ���������� == ������� def Contacts()
# ���������� request, ��� �������� ���� � ���, ��� ����� �����, ������ ������ � ��
def contacts(request):
    context = {
        'object_list': Contacts.objects.all(),
        'title': 'Наши контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html', context)


class Main_pageListView(ListView):
    model = Product
    template_name = 'catalog/main_page.html'
    extra_context = {
        'title': 'Bakery Market',
        'object_list': Category.objects.all()[:4]
    }

# def main_page(request):
#     context = {
#         'object_list': Category.objects.all()[:4],
#         'title': 'Bakery Market'
#     }
#     return render(request, 'catalog/main_page.html', context)

#def categories(request):
#    context = {
#        'object_list': Category.objects.all(),
#        'title': 'Наши вкусняши'
#    }
#    return render(request, 'catalog/category_list.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Наши вкусняши'
    }

# def product(request, pk):
#     catalog_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': f'Наши вкусняши {catalog_item.name}'
#     }
#     return render(request, 'catalog/product_list.html', context)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        """
        Возвращает выборку товаров по номеру категории
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        """
        Возвращает товары определенной категории,
        """
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Наши вкусняши {category_item.name}'

        return context_data


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    fields = ('name', 'category', 'description', 'picture', 'price',)
    # success_url = reverse_lazy('catalog:products')

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category_id])


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'category', 'description', 'picture', 'price', 'is_active')
    success_url = reverse_lazy('catalog:categories')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:categories')

