# Generated by Django 3.2.9 on 2021-11-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
