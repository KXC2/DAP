from django import forms
from .models import Register, Bank, Journal

class RegisterForm(forms.ModelForm):
    banks = forms.ModelMultipleChoiceField(
        queryset=Bank.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Register
        fields = ['name', 'surname', 'cellphone', 'banks']

class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ['CellPhone', 'Receiver', 'DepositOption', 'Amount', 'Summary']

