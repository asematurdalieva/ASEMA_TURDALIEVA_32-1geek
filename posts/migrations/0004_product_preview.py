# Generated by Django 4.2.5 on 2023-09-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_product_categories_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='post_previews'),
        ),
    ]
