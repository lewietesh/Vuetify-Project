# Generated by Django 4.0.4 on 2022-05-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.IntegerField(default=12284955317500121580, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
