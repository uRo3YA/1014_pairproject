from django.shortcuts import render
from .models import Review

# Create your views here.
def index(request):
    contents = Review.objects.all()
    context = {
        "contents": contents,
    }
    return render(request, "reviews/index.html", context)
