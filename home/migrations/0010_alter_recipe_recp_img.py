# Generated by Django 5.0.6 on 2024-06-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_recipe_recp_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recp_img',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
