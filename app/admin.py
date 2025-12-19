from django.contrib import admin
from .models import Parcel

# On ajoute la table colis dans l'interface admin
admin.site.register(Parcel)