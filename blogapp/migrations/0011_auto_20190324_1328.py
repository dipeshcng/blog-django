# Generated by Django 2.1.7 on 2019-03-24 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20190324_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatednews', to='blogapp.Category'),
        ),
    ]
