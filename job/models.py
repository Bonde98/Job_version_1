from django.db import models
from django.conf import settings

# Importer Multiselecfield .Faut le télécharger avant pip install django-multiselectfield
from multiselectfield import MultiSelectField
# from django.core.validators import MaxValueValidator
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
    objects = None
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
    objects = None
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

    JOURNEE = 'JOURNEE'
    NUIT = 'NUIT'

    HEURES_DE_TRAVAILLE = (
        (JOURNEE, 'JOURNEE'),
        (NUIT, 'NUIT')
    )

    slug = models.SlugField(max_length=30,unique=True)
    ouvrier = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='ouvrier')
    photo = models.ImageField(upload_to='photos')
    metier = models.ForeignKey(Metier,max_length=50,blank=False,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    adress_home = models.CharField(max_length=50,blank=False)
    contact = models.IntegerField(max_length=12 ,null=True)
    zone_de_deplacement = MultiSelectField(max_length=30, choices=ZONE_DE_DEPLACEMENT,max_choices=2)
    jours_de_travaille = MultiSelectField(choices=JOUR_DE_TRAVAILLE)
    heures_de_travaille = models.CharField(max_length=30, choices=HEURES_DE_TRAVAILLE)
    etoile = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='userLike_worker')

    # def number_of_likes(self):
    #     return self.likes.count()

    def __str__(self):
        return str(self.ouvrier)


