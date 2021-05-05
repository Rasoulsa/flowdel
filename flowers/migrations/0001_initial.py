# Generated by Django 3.2 on 2021-05-05 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0002_rename_customprovider_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowerColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlowerOccasions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occasion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlowerTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flower_name', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='flowers.flowercolors')),
                ('flower_provider', models.ManyToManyField(related_name='flowers', to='providers.Provider')),
                ('flower_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='flowers.flowertypes')),
                ('occasion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='flowers.floweroccasions')),
            ],
        ),
    ]
