from django.shortcuts import redirect, render
from .forms import PlaceForm
from .models import Place

def home(request):
    places = Place.objects.filter(user=request.user)

    return render(
        request,
        'places/home.html',
        {'places': places}
    )


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()
            
            return redirect('home')
    else:
        form = PlaceForm()

    return render(
        request,
        'places/add_place.html',
        {'form': form}
    )