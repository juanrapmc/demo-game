# Generated by Django 2.1.6 on 2019-02-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('position', models.IntegerField()),
                ('color', models.CharField(max_length=25)),
                ('level', models.CharField(choices=[('RE', 'Regular'), ('BX', 'Boxed'), ('CO', 'Colored')], default='RE', max_length=2)),
            ],
        ),
    ]
