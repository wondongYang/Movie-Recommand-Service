from django.urls import path
from . import views

urlpatterns = [

    path('', views.movie_list),
    path('top/<genre_name>/', views.genre_top_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('recommended/', views.movie_recommended),
]
