from django.db import models

VARIANTY_POLIVA = (
    ('редко', 'редко'),
    ('умеренно', 'умеренно'),
    ('часто', 'часто'),
)


class Semeistvo(models.Model):
    nazvanie = models.CharField(max_length=80)
    opisanie = models.TextField()

    def __str__(self):
        return self.nazvanie


class Metka(models.Model):
    nazvanie = models.CharField(max_length=50)

    def __str__(self):
        return self.nazvanie


class Rastenie(models.Model):
    nazvanie = models.CharField(max_length=80)
    latinskoe_nazvanie = models.CharField(max_length=80)
    visota_sm = models.IntegerField()
    data_pokupki = models.DateField()
    dostupno = models.BooleanField(default=True)
    poliv = models.CharField(max_length=20, choices=VARIANTY_POLIVA)
    # 1-N: семейство → растения
    semeistvo = models.ForeignKey(
        Semeistvo, on_delete=models.CASCADE, related_name='rasteniya'
    )
    # M-N: растение ↔ метки
    metki = models.ManyToManyField(Metka, related_name='rasteniya', blank=True)

    def __str__(self):
        return self.nazvanie

    @property
    def ikonka(self):
        nomer = (self.pk - 1) % 5 + 1
        return f'icons/list{nomer}.svg'


class PasportUhoda(models.Model):
    # 1-1: у растения один паспорт, удаляется вместе с растением
    rastenie = models.OneToOneField(
        Rastenie, on_delete=models.CASCADE, related_name='pasport'
    )
    osveshenie = models.CharField(max_length=120)
    temperatura = models.IntegerField()
    zametki = models.TextField(blank=True)
    data_proverki = models.DateField()

    def __str__(self):
        return f'Паспорт: {self.rastenie.nazvanie}'
