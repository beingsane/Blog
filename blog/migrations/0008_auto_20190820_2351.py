# Generated by Django 2.2.4 on 2019-08-21 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190820_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='titulo',
        ),
        migrations.AlterField(
            model_name='posts',
            name='id_post',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]