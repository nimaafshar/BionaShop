from django.db import models
from django.utils import timezone
from django.db.utils import IntegrityError


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    # image field responses to a static file in static directory
    image = models.URLField(verbose_name="image_url")

    def __str__(self):
        return self.name


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
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def total_price(self):
        total_price = 0
        for item in self.billitem_set.all():
            total_price += item.count * (item.price + item.price * item.tax_rate)

        return total_price



class BillItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    count = models.IntegerField(default=1)
    price = models.IntegerField()
    tax_rate = models.DecimalField(verbose_name="item_tax_rate", max_digits=3, decimal_places=3, default=0)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.product:
            raise IntegrityError("No product found for bill item")
        self.price = self.product.price
        super().save(*args, *kwargs)

    def __str__(self):
        return f"{self.product.name}, {self.count}"
