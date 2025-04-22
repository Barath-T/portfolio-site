"""personalsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings


from pages.views import home_view, about_view
from products.views import ProductsListView, ProductsDetailView, ProductsCreateView
from users.views import UserRegisterView, UserLogoutView, UserLoginView
from portfolio.views import ProjectListView, ProjectDetailView
from blog.views import BlogListView, BlogDetailView, ArticleCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),
    path('about/', about_view, name='about'),

    path('products/', ProductsListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductsCreateView.as_view(), name='product-create'),

    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),

    path('portfolio/projects/', ProjectListView.as_view(), name='project-list'),
    path('portfolio/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/create/', ArticleCreateView.as_view(), name='blog-create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

