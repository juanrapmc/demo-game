# Generated by Django 2.1.6 on 2019-02-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20190211_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]