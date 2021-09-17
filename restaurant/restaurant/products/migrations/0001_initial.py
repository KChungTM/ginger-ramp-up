# Generated by Django 3.2.7 on 2021-09-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('z', models.IntegerField()),
                ('category', models.TextField()),
                ('rating', models.IntegerField()),
            ],
            options={
                'ordering': ['rating'],
            },
        ),
    ]