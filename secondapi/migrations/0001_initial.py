# Generated by Django 3.0.2 on 2020-01-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('add', models.CharField(max_length=20)),
                ('contact', models.IntegerField(max_length=10)),
            ],
        ),
    ]
