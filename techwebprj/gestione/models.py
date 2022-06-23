from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''
PDF 09b_MODELSIN DETAIL
SLIDE 12

'''

'''ok
class Articolo(models.Model):
    titolo = models.CharField(max_length=200)
    dataPubblicazione = models.DateField(default=models.DateField.auto_now)
    autore = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="autore_artcolo")
'''
''' da rivedere
    def disponibile(self):
        if self.copie.filter(data_prestito=None).count() > 0:
            return True
        return False
        
    def __str__(self):
        disp = self.copie.filter(data_prestito=None).count()
        out = self.titolo + " di " + self.autore + " ha " + str(self.copie.all().count()) + " copie" + " di cui " + str(disp) + " disponibili"
        return out
    '''
'''ok
    class Meta:
        verbose_name_plural = "Articoli"
class Commento(models.Model):
    dataPubblicazione = models.DateField(default=models.DateField.auto_now)
    autore = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="autore_commento")
    articolo = models.ForeignKey(Articolo, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="articolo_commentato")

    def chi_ha_commentato(self):
        if self.utente == None: return None
        return self.autore.username
    '''
''' da rivedere
    def __str__(self):
        return "Copia di " + self.libro.titolo + " di " + self.libro.autore + " in prestito dal " + str(self.data_prestito) 
    '''
'''ok
    class Meta:
        verbose_name_plural = "Commenti"
    '''

'''
class Copia(models.Model):
    data_prestito = models.DateField(default=None,null=True,blank=True)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE,related_name="copie")
    utente = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True,default=None,related_name="copie_in_prestito")

    def chi_in_prestito(self):
        if self.utente == None: return None
        return self.utente.username

    def __str__(self):
        return "Copia di " + self.libro.titolo + " di " + self.libro.autore + " in prestito dal " + str(self.data_prestito) 

    class Meta:
        verbose_name_plural = "Copie"
    '''