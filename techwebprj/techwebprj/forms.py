from tkinter import Text
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.forms import CharField, ChoiceField, ImageField, Textarea
from gestione.models import UserProfile

class CreaUtente(UserCreationForm):
    #Facciamo un override del metodo save per assicurarci di assegnare il gruppo specificato
    #all'utente appena registrato. I gruppi possono essere creati in via programmatica, ma in questo
    #caso li abbiamo creati dal pannello admin nell'interfaccia grafica web.
    def save(self, commit=True):
        user = super().save(commit)             #ottengo un riferimento all'utente
        g = Group.objects.get(name="Utenti")    #cerco il gruppo che mi interessa
        g.user_set.add(user)                    #aggiungo l'utente al gruppo
        return user                             #restituisco quello che il metodo padre di questo metodo avrebbe restituito.


#lo cambierai prima o poi........
class CreateProfileForm(UserCreationForm):
    immagineProfilo = ImageField(required=True, label='Immagine profilo(Obbligatoria)')
    bio = CharField(label='Biografia(Opzionale)', widget=Textarea, required=False)
    mail = CharField(label='Email(Obbligatoria)', widget=Text, required=True)

    def save(self, commit= True):
        user = super().save(commit)
        user.groups.add(Group.objects.get(name="Utenti"))
        profile = UserProfile()
        profile.user = user
        profile.bio = self.cleaned_data['bio']

        tmp_img = self.cleaned_data["immagineProfilo"]
        profile.immagineProfilo = tmp_img
            
        if self.cleaned_data['public_or_private'] == 'public':
            profile.is_user_page_public = True
        else:
            profile.is_user_page_public = False
        profile.save()
        return user
