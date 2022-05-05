# Generated by Django 4.0.4 on 2022-05-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='media')),
                ('is_open', models.BooleanField(default=False)),
                ('is_known', models.BooleanField(default=False)),
            ],
        ),
    ]
