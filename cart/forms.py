from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget=forms.Select(attrs={'class': 'custom-select ml-1'}))
    override = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)
    