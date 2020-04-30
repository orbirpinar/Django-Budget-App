from django.forms import ModelForm
from django import forms

from .models import Budget


choices = (
('inc','+'),
('exp','-')

	)

class BudgetForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'add__description','placeholder' :'Add description'})
		,label='')
	amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'add__value','placeholder' :'Add values'})
		,label='')
	category = forms.ChoiceField(widget=forms.Select(attrs={'class':'add__type'}),choices=choices,label="")
	class Meta:
		model = Budget
		fields = ['name','amount','category']



