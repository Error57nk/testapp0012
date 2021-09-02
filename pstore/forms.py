from django import forms
from .models import FormCust1Model


class OrderForm1(forms.ModelForm):
    custType = forms.CharField(widget=forms.HiddenInput)
    # photoid = forms.CharField(widget=forms.HiddenInput)
    # order_from = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['detail'].widget.attrs.update(
            {'class': 'form-control', 'rows': '3', 'placeholder': 'Brif Detail of customization'})
        self.fields['note'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Note'})

    class Meta:
        model = FormCust1Model
        fields = ('custType', 'detail', 'note')
