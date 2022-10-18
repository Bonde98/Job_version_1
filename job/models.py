from django.db import models
from django.conf import settings
from authentication.models import User
from django.contrib.auth.models import User
#Class Métier
"""
-Métier
-Travailleur
-Description
-Zone de déplacement(Région et département)
-Jour de Travaille
-Heures de Travaille
-
"""
class Metier(models.Model):
    slug = models.SlugField(max_length=30,unique=True)
    nom_du_metier = models.CharField(max_length=50,verbose_name="Ton Métier")

    def __str__(self):
        return str(self.nom_du_metier)

#Class Ouvrier
"""
-Ouvrier
-photo 
-Métier
-Adresse à Domicile
-Contact
_Etoile
"""
class Worker(models.Model):
    LUNDI = 'LUNDI'
    MARDI = 'MARDI'
    MERCREDI = 'MERCREDI'
    JEUDI = 'JEUDI'
    VENDREDI = 'VENDREDI'
    SAMEDI = 'DIMANCHE'
    DIMANCHE = 'DIMANCHE'

    JOUR_DE_TRAVAILLE = (
        (LUNDI, 'LUNDI'),
        (MARDI, 'MARDI'),
        (MERCREDI, 'MERCREDI'),
        (JEUDI, 'JEUDI'),
        (VENDREDI, 'VENDREDI'),
        (SAMEDI, 'DIMANCHE'),
        (DIMANCHE, 'DIMANCHE')
    )
    DAKAR = 'DAKAR'
    THIES = 'THEIS'
    LOUGA = 'LOUGA'
    ZONE_DE_DEPLACEMENT = (
        (DAKAR, 'DAKAR'),
        (THIES, 'THEIS'),
        (LOUGA, 'LOUGA'))
    #slug = models.SlugField(max_length=30,unique=True)
    ouvrier = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='ouvrier')
    photo = models.ImageField(upload_to='photos')
    metier = models.ForeignKey(Metier,max_length=50,blank=False,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    adress_home = models.CharField(max_length=50,blank=False)
    contact = models.CharField(max_length=9,null=False)
    zone_de_deplacement = models.CharField(max_length=30, choices=ZONE_DE_DEPLACEMENT)
    jour_de_travaille = models.CharField(max_length=30, choices=JOUR_DE_TRAVAILLE)
    heure_de_travaille = models.CharField(max_length=30)
    etoile = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ouvrier)


