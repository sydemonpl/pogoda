# Generated by Django 2.1.4 on 2018-12-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Miasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Miasta',
            },
        ),
    ]
