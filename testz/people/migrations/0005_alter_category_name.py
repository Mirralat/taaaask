# Generated by Django 3.2.9 on 2021-11-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20211124_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, default='', max_length=100),
        ),
    ]