# Generated by Django 4.2 on 2023-07-28 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last_name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conclusion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TesterResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conclusion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conclusion', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_as_client', to=settings.AUTH_USER_MODEL)),
                ('tester', models.ManyToManyField(related_name='test_as_tester', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conclusion', models.TextField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.testrequirements')),
                ('testers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
