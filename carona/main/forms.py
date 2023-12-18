from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin.widgets import AdminDateWidget
from .models import Carona, Veiculo

class CaronaForm(forms.ModelForm):
    horario = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        label="Data e hora",
    )
    veiculo = forms.ModelChoiceField(
        queryset=Veiculo.objects.none(),  # Inicialize com um queryset vazio
        widget=forms.Select,  # Use o widget Select
        required=False,  # Tornar o campo opcional
        label="Veículo"
    )

    class Meta:
        model = Carona
        exclude = ('motorista',)

    def __init__(self, user, *args, **kwargs):
        super(CaronaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Cadastrar Carona'))
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'
            self.fields['origem'].widget.attrs['placeholder'] = 'Origem'
            self.fields['destino'].widget.attrs['placeholder'] = 'Destino'
            self.fields['valor'].widget.attrs['placeholder'] = 'Valor'
        self.fields['veiculo'].queryset = Veiculo.objects.filter(funcionario__user=user)
        self.fields['veiculo'].empty_label = 'Escolha um veículo:'
            
            
class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'cor', 'placa', 'capacidade']

    def __init__(self, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Adicionar', css_class='mt-3 btn-success'))
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'

class EditCaronaForm(forms.ModelForm):
    horario = forms.DateTimeField(
    widget=forms.TextInput(attrs={'type': 'datetime-local'}),
    input_formats=['%Y-%m-%dT%H:%M'],
    )
    
    class Meta:
        model = Carona
        exclude = ('motorista',)
        
    def __init__(self, *args, **kwargs):
        super(EditCaronaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Editar Carona'))
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'
            self.fields['origem'].widget.attrs['placeholder'] = 'Origem'
            self.fields['destino'].widget.attrs['placeholder'] = 'Destino'
            self.fields['valor'].widget.attrs['placeholder'] = 'Valor'
            
            