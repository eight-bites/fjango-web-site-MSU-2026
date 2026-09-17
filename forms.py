from django import forms

from .models import Metka, Semeistvo, VARIANTY_POLIVA


class FormaRasteniya(forms.Form):
    nazvanie = forms.CharField(
        max_length=80,
        error_messages={
            'required': 'Укажите название растения.',
            'max_length': 'Название слишком длинное (максимум 80 символов).',
        },
    )
    latinskoe_nazvanie = forms.CharField(
        max_length=80,
        error_messages={
            'required': 'Укажите латинское название.',
            'max_length': 'Латинское название слишком длинное (максимум 80 символов).',
        },
    )
    visota_sm = forms.IntegerField(
        min_value=1,
        error_messages={
            'required': 'Укажите высоту.',
            'invalid': 'Высота должна быть целым числом.',
            'min_value': 'Высота должна быть больше 0.',
        },
    )
    data_pokupki = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'}),
        error_messages={
            'required': 'Укажите корректную дату покупки.',
            'invalid': 'Укажите корректную дату покупки.',
        },
    )
    dostupno = forms.BooleanField(required=False, initial=True)
    poliv = forms.ChoiceField(
        choices=VARIANTY_POLIVA,
        error_messages={
            'required': 'Выберите режим полива.',
            'invalid_choice': 'Выберите режим полива.',
        },
    )
    semeistvo_id = forms.ChoiceField(
        choices=[],
        error_messages={
            'required': 'Выберите семейство.',
            'invalid_choice': 'Такого семейства нет.',
        },
    )
    metki = forms.MultipleChoiceField(required=False)
    osveshenie = forms.CharField(
        max_length=120,
        error_messages={
            'required': 'Укажите освещение.',
            'max_length': 'Текст освещения слишком длинный (максимум 120 символов).',
        },
    )
    temperatura = forms.IntegerField(
        min_value=1,
        error_messages={
            'required': 'Укажите температуру.',
            'invalid': 'Температура должна быть целым числом.',
            'min_value': 'Температура должна быть больше 0.',
        },
    )
    zametki = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea,
        error_messages={
            'max_length': 'Заметки слишком длинные (максимум 500 символов).',
        },
    )
    data_proverki = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'}),
        error_messages={
            'required': 'Укажите корректную дату проверки.',
            'invalid': 'Укажите корректную дату проверки.',
        },
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['semeistvo_id'].choices = [
            (str(s.id), s.nazvanie) for s in Semeistvo.objects.all()
        ]
        self.fields['metki'].choices = [
            (str(m.id), m.nazvanie) for m in Metka.objects.all()
        ]
        self.fields['metki'].error_messages['invalid_choice'] = (
            'Выбрана несуществующая метка.'
        )
