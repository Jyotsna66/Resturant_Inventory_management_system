from django.contrib import admin
from .models import SalesEntry, StockRequisition, DailyPurchase

@admin.register(SalesEntry)
class SalesEntryAdmin(admin.ModelAdmin):
    list_display = ('date',  'total_sale')

@admin.register(StockRequisition)
class StockRequisitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'item_name', 'item_type', 'unit', 'closing', 'required', 'delivered')

@admin.register(DailyPurchase)
class DailyPurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'item_name', 'quantity', 'price_per_unit', 'tax', 'total_price')
from django.contrib import admin

# Register your models here.
