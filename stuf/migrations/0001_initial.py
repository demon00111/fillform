# Generated by Django 3.2.7 on 2022-03-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('cpassword', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
    ]
