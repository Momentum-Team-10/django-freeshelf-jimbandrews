"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from books import views
import debug_toolbar


urlpatterns = [
    path("admin/", admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path("", views.homepage, name="home"),
    path("books/", views.book_index, name="book_index"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/", views.view_book, name="view_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/<slug:slug>/', views.view_category, name='view_category')
]
