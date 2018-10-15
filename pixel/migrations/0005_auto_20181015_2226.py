# Generated by Django 2.1.1 on 2018-10-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0004_auto_20181015_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='pixelevent',
            name='session_id',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='pixelevent',
            name='utm_campaign',
            field=models.CharField(default='None', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pixelevent',
            name='utm_content',
            field=models.CharField(default='None', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pixelevent',
            name='utm_medium',
            field=models.CharField(default='None', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pixelevent',
            name='utm_source',
            field=models.CharField(default='None', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pixelevent',
            name='utm_term',
            field=models.CharField(default='None', max_length=200, null=True),
        ),
    ]
