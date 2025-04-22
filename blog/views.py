from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect

from .forms import ArticleForm
from .models import Article

class BlogListView(ListView):
	template_name = 'blog/blog_list.html'

	queryset = Article.objects.all()


class BlogDetailView(DetailView):
	template_name = 'blog/blog_detail.html'

	queryset = Article.objects.all()

class ArticleCreateView(CreateView):
	template_name = 'blog/blog_create.html'

	form_class = ArticleForm

	queryset = Article.objects.all()

	success_url = '/blog/'



	def form_valid(self, form,):
		form.instance.author = self.request.user


		self.object = form.save()
		#do any thing with self.object
		return HttpResponseRedirect(self.get_success_url())



