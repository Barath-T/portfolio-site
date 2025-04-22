from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect

from .models import Product
from .forms import ProductForm

class ProductsListView(ListView):

	template_name = 'products/products_list.html'

	queryset = Product.objects.all()

	


class ProductsDetailView(DetailView):

	template_name = 'products/products_detail.html'

	queryset = Product.objects.all()

class ProductsCreateView(CreateView):

	template_name = 'products/products_create.html'

	form_class = ProductForm

	queryset = Product.objects.all()

	success_url = '/products/'

	def form_valid(self, form):
		self.object = form.save()
		#do any thing with self.object
		return HttpResponseRedirect(self.get_success_url())
