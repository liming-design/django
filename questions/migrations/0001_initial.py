# Generated by Django 4.1.2 on 2022-10-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('questionContent', models.CharField(max_length=200, unique=True)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
    ]
