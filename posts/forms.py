from django import forms


class CreateProductForm(forms.Form):
    preview = forms.FileField(required=False)
    name = forms.CharField(min_length=3, max_length=64)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField(max_digits=10, decimal_places=2)
