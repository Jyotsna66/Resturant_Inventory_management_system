from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('purchase_date', models.DateField()),

            ],
        ),
        migrations.CreateModel(
            name='SalesEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('sales_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StockRequisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('requisition_date', models.DateField()),
            ],
        ),
    ]
