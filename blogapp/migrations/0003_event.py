# Generated by Django 2.1.7 on 2019-03-14 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20190313_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('gallery', models.ImageField(upload_to='event')),
                ('description', models.TextField()),
                ('organizer', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]