# Generated by Django 4.0.3 on 2022-05-01 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0004_category_news_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news_site.category', verbose_name='Категория'),
        ),
    ]