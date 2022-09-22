# Generated by Django 4.1.1 on 2022-09-22 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('Phone_Number', models.CharField(max_length=10, null=True, unique=True)),
                ('Created_by', models.CharField(max_length=100)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Last_Updated_at', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='department.department')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
