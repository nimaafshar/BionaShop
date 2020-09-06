from django.forms import ModelForm
from shop.models import BillItem, Bill
from django.forms.fields import IntegerField, HiddenInput


class BillItemForm(ModelForm):
    count = IntegerField(min_value=1, max_value=100)

    class Meta:
        model = BillItem
        fields = ['count']


class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ['address', 'email', 'phone', 'first_name', 'last_name', 'postal_code']

    total_price = IntegerField(widget=HiddenInput)
