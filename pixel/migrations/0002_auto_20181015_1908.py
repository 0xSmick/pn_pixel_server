# Generated by Django 2.1.1 on 2018-10-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pixelevent',
            name='referring_url',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
    ]
