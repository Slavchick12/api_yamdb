# Generated by Django 2.2.16 on 2021-10-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20211013_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]