from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    contents = Review.objects.all()
    context = {
        "reviews": contents,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
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

