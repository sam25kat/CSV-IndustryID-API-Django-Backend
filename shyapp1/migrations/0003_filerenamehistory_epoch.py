# Generated by Django 5.1 on 2024-08-09 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shyapp1', '0002_filerenamehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerenamehistory',
            name='epoch',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
