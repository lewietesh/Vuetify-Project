# Generated by Django 4.0.4 on 2022-05-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_posts_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.IntegerField(default=11141147042029638124, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
