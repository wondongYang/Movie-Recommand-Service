from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.review_create),
    path('<int:review_pk>/', views.review_detail),
    # path('<int:review_pk>/update/', views.review_update_or_delete),
    path('<int:review_pk>/comments/create/', views.comment_create),
    path('<int:review_pk>/comments/delete/', views.comment_delete),
]
