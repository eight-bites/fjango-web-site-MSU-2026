from datetime import date

from .models import Metka, PasportUhoda, Rastenie, Semeistvo


def zaseyat():
    if Semeistvo.objects.exists():
        return

    aroidnye = Semeistvo.objects.create(
        nazvanie='Ароидные',
        opisanie='Тропические растения с крупными листьями, часто лианы.',
    )
    kaktusovye = Semeistvo.objects.create(
        nazvanie='Кактусовые',
        opisanie='Суккуленты с колючками, родом из засушливых мест.',
    )
    tolstyankovye = Semeistvo.objects.create(
        nazvanie='Толстянковые',
        opisanie='Мясистые листья, запасают воду.',
    )
    marantovye = Semeistvo.objects.create(
        nazvanie='Марантовые',
        opisanie='Декоративно-лиственные растения влажных лесов.',
    )

    ten = Metka.objects.create(nazvanie='теневыносливое')
    cvet = Metka.objects.create(nazvanie='цветущее')
    sukkulent = Metka.objects.create(nazvanie='суккулент')
    vozduh = Metka.objects.create(nazvanie='очищает воздух')
    yadovitoe = Metka.objects.create(nazvanie='ядовитое')
    vlaga = Metka.objects.create(nazvanie='влаголюбивое')

    monstera = Rastenie.objects.create(
        nazvanie='Монстера деликатесная',
        latinskoe_nazvanie='Monstera deliciosa',
        visota_sm=120,
        data_pokupki=date(2024, 3, 12),
        dostupno=True,
        poliv='умеренно',
        semeistvo=aroidnye,
    )
    monstera.metki.set([ten, vozduh, yadovitoe])
    PasportUhoda.objects.create(
        rastenie=monstera,
        osveshenie='яркий рассеянный свет',
        temperatura=22,
        zametki='Протирать листья от пыли раз в неделю.',
        data_proverki=date(2026, 9, 1),
    )

    epipremnum = Rastenie.objects.create(
        nazvanie='Эпипремнум золотистый',
        latinskoe_nazvanie='Epipremnum aureum',
        visota_sm=45,
        data_pokupki=date(2023, 11, 5),
        dostupno=True,
        poliv='умеренно',
        semeistvo=aroidnye,
    )
    epipremnum.metki.set([ten, vozduh])
    PasportUhoda.objects.create(
        rastenie=epipremnum,
        osveshenie='полутень',
        temperatura=20,
        zametki='Хорошо растёт на полке в коридоре.',
        data_proverki=date(2026, 8, 20),
    )

    ehinopsis = Rastenie.objects.create(
        nazvanie='Эхинопсис острогранный',
        latinskoe_nazvanie='Echinopsis oxygona',
        visota_sm=18,
        data_pokupki=date(2025, 1, 20),
        dostupno=True,
        poliv='редко',
        semeistvo=kaktusovye,
    )
    ehinopsis.metki.set([sukkulent, cvet])
    PasportUhoda.objects.create(
        rastenie=ehinopsis,
        osveshenie='прямое солнце утром',
        temperatura=25,
        zametki='Зимой почти не поливать.',
        data_proverki=date(2026, 7, 15),
    )

    krassula = Rastenie.objects.create(
        nazvanie='Крассула овальная',
        latinskoe_nazvanie='Crassula ovata',
        visota_sm=30,
        data_pokupki=date(2022, 9, 1),
        dostupno=False,
        poliv='редко',
        semeistvo=tolstyankovye,
    )
    krassula.metki.set([sukkulent])
    PasportUhoda.objects.create(
        rastenie=krassula,
        osveshenie='яркий свет',
        temperatura=21,
        zametki='Отдан в другой корпус на выставку.',
        data_proverki=date(2026, 6, 10),
    )

    kalatea = Rastenie.objects.create(
        nazvanie='Калатея орната',
        latinskoe_nazvanie='Calathea ornata',
        visota_sm=55,
        data_pokupki=date(2024, 7, 8),
        dostupno=True,
        poliv='часто',
        semeistvo=marantovye,
    )
    kalatea.metki.set([vlaga, ten])
    PasportUhoda.objects.create(
        rastenie=kalatea,
        osveshenie='тень, без прямого солнца',
        temperatura=23,
        zametki='Любит влажный воздух, рядом поставить миску с водой.',
        data_proverki=date(2026, 9, 10),
    )
