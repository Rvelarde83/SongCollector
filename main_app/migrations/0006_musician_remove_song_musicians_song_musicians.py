# Generated by Django 4.0.6 on 2022-07-19 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_song_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='musicians',
        ),
        migrations.AddField(
            model_name='song',
            name='musicians',
            field=models.ManyToManyField(to='main_app.musician'),
        ),
    ]
