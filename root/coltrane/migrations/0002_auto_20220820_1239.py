# Generated by Django 3.2.6 on 2022-08-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coltrane', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Maximum 250 characters.', max_length=250),
        ),
    ]
