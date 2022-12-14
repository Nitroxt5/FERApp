# Generated by Django 4.1.3 on 2022-12-13 07:30

import django.core.validators
from django.db import migrations, models
import main.models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=main.models.get_upload_to, validators=[main.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(' ', 'Title must not contain spaces!', code='invalid_text', inverse_match=True)]),
        ),
    ]
