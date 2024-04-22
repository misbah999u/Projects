# Generated by Django 2.2.5 on 2019-09-15 15:09

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('active', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_veg', models.BooleanField()),
                ('quantity', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.FoodCategory')),
            ],
        ),
    ]
