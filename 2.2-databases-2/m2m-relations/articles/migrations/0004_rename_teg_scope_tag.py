# Generated by Django 4.1.2 on 2022-10-19 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='teg',
            new_name='tag',
        ),
    ]