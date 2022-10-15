from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
    path("movie/", views.movie_list, name="movie"),
    path("movie/<int:movie_pk>", views.movie_detail, name="movie_detail"),
    path("movie/<int:movie_pk>/create/", views.review_create, name="review_create"),
    path("<int:review_pk>/review_detail", views.review_detail, name="review_detail"),
    path("<int:review_pk>/review_update", views.review_update, name="review_update"),
    path("<int:review_pk>/review_delete", views.review_delete, name="review_delete"),
]
