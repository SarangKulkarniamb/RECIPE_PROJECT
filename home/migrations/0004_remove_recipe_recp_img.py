# Generated by Django 5.0.6 on 2024-06-20 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_recipe_recp_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recp_img',
        ),
    ]
