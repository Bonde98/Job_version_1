from django import forms
from .models import Worker

#Formulaire de Worker
class WorkerForm(forms.ModelForm):
    # Modifier le profil Travailleur
    edit_worker = forms.BooleanField(widget=forms.HiddenInput,initial=True)

    class Meta:
        model = Worker
        fields = ['metier','bio','adress_home','contact','zone_de_deplacement','jour_de_travaille']


class DeleteWorkerForm(forms.Form):
    # Supprimer le profil Travailleur
    delete_worker = forms.BooleanField(widget=forms.HiddenInput, initial=True)