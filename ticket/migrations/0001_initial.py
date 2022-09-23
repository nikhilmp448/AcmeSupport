# Generated by Django 4.1.1 on 2022-09-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ticket_ID', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('Priority', models.CharField(max_length=100)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
