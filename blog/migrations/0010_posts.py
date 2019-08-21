# Generated by Django 2.2.4 on 2019-08-21 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0009_delete_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=20)),
                ('data', models.DateTimeField(verbose_name='Post Date')),
                ('semestre', models.IntegerField(verbose_name='Semestre')),
                ('discplina', models.CharField(max_length=50)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]