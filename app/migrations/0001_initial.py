# Generated by Django 4.1.7 on 2023-05-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]