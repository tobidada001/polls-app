# Generated by Django 4.1 on 2022-10-07 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Naaew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PollTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(default='First option', max_length=50)),
                ('choice_id', models.IntegerField()),
                ('choice_polltitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatedchoice', to='pollsapp.polltitle')),
            ],
        ),
    ]
