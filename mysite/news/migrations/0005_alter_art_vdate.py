# Generated by Django 3.2 on 2021-05-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210531_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='vdate',
            field=models.DateField(default='31-05-2021', verbose_name='vДата'),
        ),
    ]
