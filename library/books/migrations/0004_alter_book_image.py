# Generated by Django 5.0.6 on 2024-05-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='media/%Y/%m/%d'),
        ),
    ]