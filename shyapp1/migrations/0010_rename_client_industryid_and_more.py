# Generated by Django 5.1 on 2024-08-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shyapp1', '0009_alter_filerenamehistory_epoch'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='IndustryID',
        ),
        migrations.RenameField(
            model_name='filerenamehistory',
            old_name='client',
            new_name='industryid',
        ),
        migrations.AlterField(
            model_name='filerenamehistory',
            name='epoch',
            field=models.IntegerField(default=1723203775),
        ),
    ]