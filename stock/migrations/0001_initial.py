# Generated by Django 3.0.7 on 2020-06-18 23:06

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='parent_company', to='company.Company')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listed_exchange', to='exchange.Exchange')),
            ],
        ),
        migrations.CreateModel(
            name='StockPriceData',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('high', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=15)),
                ('low', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=15)),
                ('open', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=15)),
                ('close', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=15)),
                ('volume', models.BigIntegerField(blank=True, null=True)),
                ('change', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=15)),
                ('change_perc', models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=15)),
                ('ml_prediction', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL'), ('HOLD', 'HOLD'), ('N/A', 'N/A')], default='HOLD', max_length=4)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_data', to='stock.Stock')),
            ],
            options={
                'verbose_name': 'Stock Price Data',
                'verbose_name_plural': 'Stocks Price Data',
                'db_table': 'stock_price',
            },
        ),
        migrations.AddIndex(
            model_name='stockpricedata',
            index=models.Index(fields=['timestamp', 'stock'], name='stock_price_timesta_0d32c7_idx'),
        ),
        migrations.AddConstraint(
            model_name='stockpricedata',
            constraint=models.UniqueConstraint(fields=('stock', 'timestamp'), name='unique_stock_data'),
        ),
        migrations.AddConstraint(
            model_name='stock',
            constraint=models.UniqueConstraint(fields=('ticker', 'name', 'exchange_id'), name='exchange_stock'),
        ),
    ]