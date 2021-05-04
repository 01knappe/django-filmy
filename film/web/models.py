
from django.db import models

# Create your models here.
from django.urls import reverse


class Zanr(models.Model):
    zanr = models.CharField(max_length=20, unique=True, verbose_name="Žánr",
                            help_text='Zadejte text o maximální délce 20 znaků')

    class Meta:
        ordering = ["zanr"]

    def __str__(self):
        return f"{self.zanr}"


class Film(models.Model):

    nazev = models.CharField(max_length=50, verbose_name="Nazev")
    stat = models.CharField(blank=True, null=True, max_length=50, verbose_name="Stát")
    rezie = models.CharField(blank=True, null=True, max_length=60, verbose_name="Režie")
    scenar = models.CharField(blank=True, null=True, max_length=60, verbose_name="Scénář")
    rok = models.IntegerField(blank=True, null=True, verbose_name="Rok vydani")
    obsah = models.TextField(blank=True, null=True, verbose_name="Obsah")
    zanr = models.ForeignKey(Zanr, on_delete=models.RESTRICT)
    foto = models.ImageField(upload_to='film/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka filmu")



    class Meta:

        ordering = ["nazev"]

    def __str__(self):
        return f"{self.nazev}, {self.rok}"

    def get_absolute_url(self):

        return reverse('detail', args=[str(self.id)])









