from django import forms

class AddDishForm(forms.Form):
    dish_id = forms.IntegerField()
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    availability = forms.BooleanField(required=False)


class TakeOrderForm(forms.Form):
    items = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)
    quantities = forms.CharField(max_length=100)
    customer_name = forms.CharField(max_length=100)

