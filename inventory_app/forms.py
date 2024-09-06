from django import forms
from .models import SalesEntry, DailyPurchase, StockRequisition

class SalesEntryForm(forms.ModelForm):
    class Meta:
        model = SalesEntry
        fields = ['date', 'phonepe_upi', 'card_pmt', 'zomato', 'swiggy', 'bms', 'cash', 'expenditure']

class DailyPurchaseForm(forms.ModelForm):
    class Meta:
        model = DailyPurchase
        fields = ['date', 'item_name', 'quantity', 'tax', 'price_per_unit']

class StockRequisitionForm(forms.ModelForm):
    class Meta:
        model = StockRequisition
        fields = ['date', 'item_type', 'item_name', 'unit', 'closing', 'required', 'delivered']
