# Generated by Django 3.1 on 2020-09-03 11:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='costumer_address')),
                ('email', models.EmailField(max_length=254, verbose_name='costumer_email')),
                ('phone', models.CharField(max_length=11, verbose_name='costumer_phone_number')),
                ('first_name', models.CharField(max_length=50, verbose_name='costumer_first_name')),
                ('last_name', models.CharField(max_length=100, verbose_name='costumer_last_name')),
                ('postal_code', models.CharField(max_length=10, verbose_name='costumer_postal_code')),
                ('status', models.CharField(choices=[('SUB', 'Submitted'), ('ACC', 'Accepted'), ('REJ', 'Rejected'), ('SHP', 'Shipping'), ('DLV', 'Delivered')], default='SUB', max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.URLField(verbose_name='image_url')),
            ],
        ),
        migrations.CreateModel(
            name='BillItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('tax_rate', models.DecimalField(decimal_places=3, max_digits=3, verbose_name='item_tax_rate')),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bill')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product')),
            ],
        ),
    ]
