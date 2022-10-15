from django import forms
from .models import Review, Movie


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "star",
        ]


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
