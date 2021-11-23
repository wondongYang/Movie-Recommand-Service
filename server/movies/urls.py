from django.urls import path
from . import views

urlpatterns = [

    path('', views.movie_list),
    path('latest/', views.latest_movie_list),
    path('top_reviews/', views.review_desc_movie_list),
    path('top/<genre_name>/', views.genre_top_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/likes/', views.movie_likes),
    path('recommended/', views.movie_recommended),
    # path('recommended/model1/', views.movie_recommended_model1),
    path('search/', views.movie_search_list),
]
