# Generated by Django 3.1.3 on 2020-12-15 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taskDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=30)),
                ('priority', models.CharField(max_length=30)),
                ('completed', models.BooleanField(default=False)),
                ('time_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
