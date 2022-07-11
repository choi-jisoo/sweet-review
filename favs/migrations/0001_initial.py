# Generated by Django 2.2.5 on 2022-07-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('books', models.ManyToManyField(blank=True, related_name='fav_lists', to='books.Book')),
            ],
            options={
                'verbose_name': 'Favourite List',
            },
        ),
    ]