# Generated by Django 5.1.3 on 2024-11-22 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_remove_chaivariety_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
