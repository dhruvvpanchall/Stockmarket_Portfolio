# Generated by Django 4.2.5 on 2023-09-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Close1', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Close2', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Close3', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Close4', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Close5', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Close6', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Close7', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Close8', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Close9', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
