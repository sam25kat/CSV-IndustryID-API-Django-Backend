# Generated by Django 5.1 on 2024-08-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shyapp1', '0004_alter_filerenamehistory_epoch'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerenamehistory',
            name='new_file_path',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filerenamehistory',
            name='epoch',
            field=models.IntegerField(default=1723195385),
        ),
    ]
