# Generated by Django 2.0 on 2017-12-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailylog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]