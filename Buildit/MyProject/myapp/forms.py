from django import forms
from django.forms import ModelForm
from myapp.models import *

class ProdutoForm(forms.ModelForm):
    class Meta:

        model = Produto
        fields = "__all__"
        labels = {
            "name": "nome",
            "descript": "descrição",
            "price": "preço",
            "path": "imagem",
            "amount": "quantidade",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do item",
                }
            ),
            'descript': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva uma breve descrição",
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "150.00",
                }
            ),
            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "50",
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Imagem",
                }
            ),
        }