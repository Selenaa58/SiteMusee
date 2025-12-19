from django.db import models

"""
0 : colis enregistré
1 : colis envoyé
2 : colis en transit
3 : colis en livraison
4 : colis livré
5 : probleme de livraison
"""

# Create your models here.
class Parcel(models.Model):
    tracking_number = models.CharField(max_length=16)
    adress_dep = models.CharField(max_length=200)
    adress_arr = models.CharField(max_length=200)
    weight = models.IntegerField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return f"Colis n°{self.tracking_number}"
