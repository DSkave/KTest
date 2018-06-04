# Generated by Django 2.0.2 on 2018-05-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OddsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=30)),
                ('corse_type', models.CharField(max_length=30, null=True)),
                ('race_no', models.IntegerField()),
                ('horse_no', models.IntegerField()),
                ('win_odds', models.DecimalField(decimal_places=1, max_digits=4)),
                ('show_odds1', models.DecimalField(decimal_places=1, max_digits=4)),
                ('show_odds2', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
    ]