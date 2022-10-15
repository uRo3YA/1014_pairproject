from django.shortcuts import render, redirect
from .models import Review, Movie
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    contents = Review.objects.all()
    context = {
        "reviews": contents,
    }
    return render(request, "reviews/index.html", context)


@login_required
def create(request, movie_pk):
    info = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new = review_form.save(commit=False)
            new.movie_id = info.pk
            new.movie_name = info.title
            new.grade = len(new.star)
            new.writer = request.user
            new.save()
            return redirect("reviews:movie_detail", info.pk)
    else:
        review_form = ReviewForm()
    context = {"review_form": review_form}
    return render(request, "reviews/create.html", context=context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {"review": review}
    return render(request, "reviews/detail.html", context)


def delete(request, pk):

    review = Review.objects.get(pk=pk)
    review.delete()

    return redirect("reviews:index")


def update(request, pk):
    movie = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=movie)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:detail", movie.pk)
    else:
        review_form = ReviewForm(instance=movie)
    context = {"review_form": review_form}
    return render(request, "reviews/update.html", context)


def movie_list(request):
    contents = Movie.objects.all()
    context = {
        "contents": contents,
    }
    return render(request, "reviews/movie_list.html", context)


def movie_detail(request, movie_pk):
    info = Movie.objects.get(pk=movie_pk)
    review = Review.objects.filter(movie_id=info.pk)
    context = {
        "info": info,
        "reviews": review,
    }
    return render(request, "reviews/movie_detail.html", context)


@login_required
def review_create(request, movie_pk):
    info = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new = review_form.save(commit=False)
            new.movie_id = info.pk
            new.movie_name = info.title
            new.grade = len(new.star)
            new.writer = request.user
            new.save()
            return redirect("reviews:movie_detail", info.pk)
    else:
        review_form = ReviewForm()
    context = {"review_form": review_form}
    return render(request, "reviews/create.html", context=context)


def review_detail(request, review_pk):
    info = Review.objects.get(pk=review_pk)
    context = {
        "info": info,
    }
    return render(request, "reviews/review_detail.html", context)


@login_required
def review_update(request, review_pk):
    info = Review.objects.get(pk=review_pk)
    if info.writer == request.user:
        if request.method == "POST":
            review_form = ReviewForm(request.POST, instance=info)
            if review_form.is_valid():
                review_form.save()
                return redirect("reviews:review_detail", info.pk)
        else:
            review_form = ReviewForm(instance=info)
        context = {
            "review_form": review_form,
        }
    else:
        return redirect("reviews:movie_detail", info.pk)

    return render(request, "reviews/review_update.html", context)


@login_required
def review_delete(request, review_pk):
    info = Review.objects.get(pk=review_pk)
    movie_id = info.movie_id
    if info.writer == request.user:
        info.delete()
    return redirect("reviews:movie_detail", movie_id)
