
from django.db import models

class SalesEntry(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    phonepe_upi = models.DecimalField(max_digits=10, decimal_places=2)
    card_pmt = models.DecimalField(max_digits=10, decimal_places=2)
    zomato = models.DecimalField(max_digits=10, decimal_places=2)
    swiggy = models.DecimalField(max_digits=10, decimal_places=2)
    bms = models.DecimalField(max_digits=10, decimal_places=2)
    cash = models.DecimalField(max_digits=10, decimal_places=2)
    expenditure = models.DecimalField(max_digits=10, decimal_places=2)
    total_sale = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        # Calculate total_sale by summing up all payment methods and subtracting expenditure
        self.total_sale = (
            self.phonepe_upi + self.card_pmt + self.zomato +
            self.swiggy + self.bms + self.cash - self.expenditure
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sales Entry {self.id} on {self.date}"



class StockRequisition(models.Model):
    date = models.DateField()
    item_type = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    closing = models.FloatField()
    required = models.FloatField()
    delivered = models.FloatField()

    def __str__(self):
        return f"{self.item_name} ({self.date})"




class DailyPurchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    item_name = models.CharField(max_length=100)  # Name of the purchased item
    quantity = models.FloatField()
    tax = models.DecimalField(max_digits=10, decimal_places=2)  # Specify max_digits and decimal_places
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        # Calculate total_price by multiplying quantity with price_per_unit and adding tax
        self.total_price = (self.quantity * self.price_per_unit) + self.tax
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.item_name} ({self.date})"



