from django import forms
# from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

from .models import Oracion


class OracionUpdateForm(forms.ModelForm):
    class Meta:
        model = Oracion
        fields = ['motivo']


class OracionAddForm(forms.ModelForm):
    class Meta:
        model = Oracion
        fields = ['nombre', 'fecha_hora', 'motivo']
        labels = {
            'nombre': 'Tu nombre',
            'fecha_hora': 'Fecha y Hora en la que vas a orar',
            'motivo': '¿Por quién o por qué vas a orar en el bando de oración?',
        }
        help_texts = {
            'nombre': 'Puede ser tu nombre o la familia',
            'fecha_hora': 'La hora en la que dedicaras el tiempo para orar',
            'motivo': 'Aquí expresa los motivos de tu oración, una persona, una familia, etc.',
        }
        widgets = {
            'fecha_hora': forms.DateInput(attrs={'id': 'datetimepicker'})
        }
        # widgets = {
        #     'fecha_hora': DateTimePickerInput(
        #         options={
        #             "format": "DD/MM/YYYY HH:00",
        #             "locale": "es-mx",
        #         }
        #     ),
        # }
