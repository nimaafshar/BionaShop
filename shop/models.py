from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()


class Bill(models.Model):
    bill_status_choices = [
        ('SUB', 'Submitted'),
        ('ACC', 'Accepted'),
        ('REJ', 'Rejected'),
        ('SHP', 'Shipping'),
        ('DLV', 'Delivered')
    ]
    address = models.TextField("costumer_address")
    email = models.EmailField("costumer_email")
    phone = models.CharField(max_length=11, verbose_name="costumer_phone_number")
    first_name = models.CharField(max_length=50, verbose_name="costumer_first_name")
    last_name = models.CharField(max_length=100, verbose_name="costumer_last_name")
    postal_code = models.CharField(max_length=10, verbose_name="costumer_postal_code")
    status = models.CharField(max_length=10, choices=bill_status_choices, default='SUB', null=False)


class BillItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    count = models.IntegerField()
    price = models.IntegerField()
    tax_rate = models.DecimalField(verbose_name="item_tax_rate", max_digits=0, decimal_places=3)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
