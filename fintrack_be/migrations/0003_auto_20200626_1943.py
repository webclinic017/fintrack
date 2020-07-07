# Generated by Django 3.0.7 on 2020-06-26 19:43

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fintrack_be', '0002_auto_20200626_1603'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='position',
            name='fintrack_be_id_82b954_idx',
        ),
        migrations.AddField(
            model_name='position',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='position',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='position_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='funds',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=15),
        ),
        migrations.AddField(
            model_name='user',
            name='result',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=15),
        ),
        migrations.AddField(
            model_name='user',
            name='value',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=15),
        ),
        migrations.AlterField(
            model_name='position',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position_stock', to='fintrack_be.Stock'),
        ),
        migrations.AddIndex(
            model_name='position',
            index=models.Index(fields=['id', 'instrument', 'user'], name='fintrack_be_id_47ebb5_idx'),
        ),
        migrations.AddConstraint(
            model_name='position',
            constraint=models.UniqueConstraint(fields=('id', 'user', 'instrument'), name='unique_position'),
        ),
    ]