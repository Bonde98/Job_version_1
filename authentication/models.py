from django.db import models
from django.contrib.auth.models import  AbstractUser, Group
# Create your models here.


"""
Class 
-Nom
-Prénom
-Email
-Adresse domicile
-photo de profile
-Contact téléphone
-Sexe
-Role (Travailleur ou Abonné  )
"""
#Class Utilisateur
class User(AbstractUser):
    WORKER = 'WORKER'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (WORKER, 'Trvailleur'),
        (SUBSCRIBER,'Abonné')
    )
    HOMME = 'HOMME'
    FEMME = 'FEMME'
    SEXE_CHOICES = (
        (HOMME, 'Homme'),
        (FEMME, 'Femme')
    )
    #home_adress = models.CharField(max_length=200,null=False,verbose_name='Adresse domicile')
    profile_photo = models.ImageField(verbose_name='Photo de profile',upload_to='photo_de_profile')
    #numbers = models.CharField(unique=True,max_length=9,verbose_name='Numéro Téléphone')
    sexe = models.CharField(max_length=30,choices=SEXE_CHOICES,verbose_name='Sexe')
    role = models.CharField(max_length=30,choices=ROLE_CHOICES,verbose_name='Role')

    # def __str__(self):
    #     return self.username

    # Nouvelle methode save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.WORKER:
            group = Group.objects.get(name='workers')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)

