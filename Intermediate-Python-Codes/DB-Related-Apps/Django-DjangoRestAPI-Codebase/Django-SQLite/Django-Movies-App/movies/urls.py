"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from movies import views

urlpatterns = [
    # This is the URL for the Django Admin site
    path('admin/', admin.site.urls),
    # this will call the movies() function under views.py
    path('movies/', views.movies),
    # this will call the movies() function under views.py
    # Empty String cause by default we want them to come to the homepage
    path('', views.home),
    # To Get the ID as a URL param
    path( 'movies/<int:id>', views.movieDetail),
    path( 'movies/add', views.addMovie),
    path( 'movies/deleteMovie/<int:id>', views.deleteMovie)
]
