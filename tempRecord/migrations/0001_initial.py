# Generated by Django 4.0 on 2021-12-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tempRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=5)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('room_id', models.IntegerField(null=True)),
            ],
        ),
    ]