# Generated by Django 2.2.1 on 2019-05-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(),
        ),
    ]
