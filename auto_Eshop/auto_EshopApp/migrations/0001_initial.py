# Generated by Django 4.2.1 on 2023-06-22 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('distance_travelled', models.CharField(max_length=250)),
                ('first_registration', models.DateField()),
                ('gearbox', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic'), ('Semi-automatic', 'Semi-automatic')], max_length=250)),
                ('number_of_owners', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('date_created', models.DateField(auto_now=True)),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auto_EshopApp.vehicle')),
                ('note', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_EshopApp.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_EshopApp.customuser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_EshopApp.post')),
            ],
        ),
    ]