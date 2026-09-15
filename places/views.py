from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django.shortcuts import redirect, render
from .forms import PlaceForm
from .models import Place

@login_required(login_url='login')
def home(request):
    places = Place.objects.filter(user=request.user)

    return render(
        request,
        'places/home.html',
        {'places': places}
    )

@login_required(login_url='login')
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

def home(request):
    if request.user.is_authenticated:
        places = Place.objects.filter(user=request.user)
    else:
        places = Place.objects.none()

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

def place_detail(request, place_id):
    place = Place.objects.get(
        id=place_id,
        user=request.user
    )

    return render(
        request,
        'places/place_detail.html',
        {'place': place}
    )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')
    else:
        form = UserCreationForm()

    return render(
        request,
        'places/register.html',
        {'form': form}
    )


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            login(request, form.get_user())

            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(
        request,
        'places/login.html',
        {'form': form}
    )


def logout_view(request):
    logout(request)

    return redirect('login')