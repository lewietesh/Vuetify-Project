# Generated by Django 4.0.4 on 2022-05-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_posts_author_alter_posts_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.BigAutoField(default=51533879819366955281269318120, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
