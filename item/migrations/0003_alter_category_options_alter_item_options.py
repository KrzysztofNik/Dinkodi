# Generated by Django 4.2.1 on 2023-10-16 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-created_at',)},
        ),
    ]
