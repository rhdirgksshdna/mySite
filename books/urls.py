"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include
from . import views

app_name = 'books'
urlpatterns = [
    # /books/
    path('', views.BoooksModelView.as_view(), name='index'),

    # /books/book
    path('book/', views.BookList.as_view(), name='book_list'),

    # /bokks/author
    path('author/', views.AuthorList.as_view(), name='author_list'),

    # /bokks/publisher
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),

    # /books/book/99
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),

    # /books/author/99/
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),

    # /books/publisher/99
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
]