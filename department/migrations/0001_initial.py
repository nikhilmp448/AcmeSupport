# Generated by Django 4.1.1 on 2022-09-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=500)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Last_Updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
