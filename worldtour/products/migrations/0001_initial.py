# Generated by Django 5.1.7 on 2025-03-20 22:48

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('icon_url', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_categories', to='products.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('subtitle', models.CharField(blank=True, max_length=512)),
                ('image1_url', models.URLField(blank=True, null=True)),
                ('image2_url', models.URLField(blank=True, null=True)),
                ('image3_url', models.URLField(blank=True, null=True)),
                ('image4_url', models.URLField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('curency', models.CharField(choices=[('USD', 'United States Dollar'), ('EUR', 'Euro'), ('JOD', 'Jordanian Dinar')], default='JOD', max_length=3)),
                ('variation_porduct_id', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None)),
                ('Provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.provider')),
            ],
        ),
    ]
