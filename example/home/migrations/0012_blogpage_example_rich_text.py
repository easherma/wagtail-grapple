# Generated by Django 2.2.1 on 2019-08-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190819_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='example_rich_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]