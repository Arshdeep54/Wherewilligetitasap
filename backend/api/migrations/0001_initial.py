# Generated by Django 4.2.6 on 2023-10-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=512)),
                ('pin_code', models.IntegerField()),
                ('address', models.CharField(max_length=256)),
            ],
        ),
    ]
