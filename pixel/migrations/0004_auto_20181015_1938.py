# Generated by Django 2.1.1 on 2018-10-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0003_pixelevent_ga_cookie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pixelevent',
            name='ga_cookie_id',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
