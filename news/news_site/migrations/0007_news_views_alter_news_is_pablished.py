# Generated by Django 4.0.3 on 2022-06-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0006_alter_news_is_pablished'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_pablished',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
    ]