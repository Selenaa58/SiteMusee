from django.http import HttpResponse
from django.shortcuts import render
from .models import Parcel
from .forms import ParcelForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save() # sauvegarde le modele / insert dans la db
    else:
        form = ParcelForm()
    return render(request, "register.html", {'form': form})

def parcel_page(request):
    parcels = Parcel.objects.all()
    return render(
        request, 
        "parcels.html", 
        context={'parcels': parcels, 'nb_parcels': len(parcels)}
    )

def one_parcel_page(request, id): 
    # recuperer un colis specifique avec son id
    one_parcel = Parcel.objects.get(id=id)
    return render(request, "one_parcel.html", context={'one_parcel': one_parcel})