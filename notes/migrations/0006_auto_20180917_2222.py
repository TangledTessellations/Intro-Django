# Generated by Django 2.1.1 on 2018-09-17 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20180917_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_tag',
            field=models.CharField(default='NS', max_length=200),
        ),
    ]