# Generated by Django 4.0.4 on 2022-05-18 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_posts_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='id',
            new_name='article_id',
        ),
    ]
