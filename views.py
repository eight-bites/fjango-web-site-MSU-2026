from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import FormaRasteniya
from .models import Metka, PasportUhoda, Rastenie, Semeistvo
from .seeds import zaseyat


def _semena():
    try:
        zaseyat()
    except Exception:
        pass


def glavnaya(request):
    _semena()
    rasteniya = Rastenie.objects.all()
    semeistva = Semeistvo.objects.all()
    return render(request, 'index.html', {
        'rasteniya': rasteniya,
        'semeistva': semeistva,
    })


def katalog(request):
    _semena()
    rasteniya = Rastenie.objects.select_related('semeistvo')
    return render(request, 'catalog.html', {'rasteniya': rasteniya})


def kartochka(request, id):
    rastenie = get_object_or_404(
        Rastenie.objects.select_related('semeistvo', 'pasport'),
        pk=id,
    )
    return render(request, 'detail.html', {'rastenie': rastenie})


def dobavit(request):
    _semena()
    semeistva = Semeistvo.objects.all()
    metki = Metka.objects.all()

    if request.method == 'POST':
        forma = FormaRasteniya(request.POST)
        if forma.is_valid():
            data = forma.cleaned_data
            rastenie = Rastenie.objects.create(
                nazvanie=data['nazvanie'],
                latinskoe_nazvanie=data['latinskoe_nazvanie'],
                visota_sm=data['visota_sm'],
                data_pokupki=data['data_pokupki'],
                dostupno=data['dostupno'],
                poliv=data['poliv'],
                semeistvo_id=int(data['semeistvo_id']),
            )
            rastenie.metki.set(data['metki'])
            PasportUhoda.objects.create(
                rastenie=rastenie,
                osveshenie=data['osveshenie'],
                temperatura=data['temperatura'],
                zametki=data['zametki'],
                data_proverki=data['data_proverki'],
            )
            return redirect('katalog')
    else:
        forma = FormaRasteniya()

    return render(request, 'add.html', {
        'forma': forma,
        'semeistva': semeistva,
        'metki': metki,
    })


@require_POST
def udalit(request, id):
    rastenie = get_object_or_404(Rastenie, pk=id)
    rastenie.delete()
    return redirect('katalog')
