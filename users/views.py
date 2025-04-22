from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect

from .forms import RegisterForm
from .models import User

class UserRegisterView(CreateView):
	template_name = 'users/register.html'

	form_class = RegisterForm

	queryset = User.objects.all()

	def get_success_url(self):
		return '/login/'

	def form_valid(self, form):
		self.object = form.save()
		#do anythig with self.object
		return HttpResponseRedirect(self.get_success_url())

class UserLoginView(LoginView):

	template_name = 'users/login.html'


class UserLogoutView(LogoutView):

	template_name = 'users/logout.html'

