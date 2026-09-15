from django.shortcuts import redirect, render

from .forms import PlaceForm
from .models import Place

def home(request):
    places = Place.objects.all()

    return render(
        request,
        'places/home.html',
        {'places': places}
    )


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlaceForm()

    return render(
        request,
        'places/add_place.html',
        {'form': form}
    )