from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''
PDF 09b_MODELSIN DETAIL
SLIDE 12
'''

''''
le parole del professor oak rimbombano nella tua testa: non ti azzardare ad usare una primary key diverse da quelle di default
'''
#per la gestione delle immagini installa pillow sotto consiglio del supremo

class Articolo(models.Model):
    titolo = models.CharField(max_length=128)
    dataPubblicazione = models.DateField(default=timezone.now)
    autore = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="autore_artcolo")
    corpo = models.TextField(default="Testo-mancante") #<----- controlla cosa mettere dentro
    dataUltimaModifica = models.DateField(default=timezone.now)
    profile_img = models.ImageField(upload_to='imgs/immaginiArticoli/', default=None)

    class Meta:
        verbose_name_plural = "Articoli"

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profilo')
    immagineProfilo = models.ImageField(upload_to='imgs/immaginiProfilo/', default=None)
    bio = models.TextField(default="")
    seguiti = models.ManyToManyField(to=Articolo, related_name='se_seguito')
    mail = models.CharField(max_length=128)

    '''
    def is_editor(self):
        editor_group = Group.objects.filter(name="Editor").first()
        return editor_group in self.user.groups.all() or self.user.is_superuser
    '''

class Commento(models.Model):
    dataPubblicazione = models.DateField(default=timezone.now)
    autore = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="autore_commento")
    articolo = models.ForeignKey(Articolo, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="articolo_commentato")
    testo = models.TextField(default="erroreLetturaTesto") #<----- controlla cosa mettere dentro

    class Meta:
        verbose_name_plural = "Commenti"

class Messaggio(models.Model):
    data = models.DateField(default=timezone.now)
    mittente = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="mittente")
    destinatario = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="destinatario")
    testo = models.TextField(default="Testo-mancante") #<----- controlla cosa mettere dentro

    class Meta:
        verbose_name_plural = "Messaggi"
