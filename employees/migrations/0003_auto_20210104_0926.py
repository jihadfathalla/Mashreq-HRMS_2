# Generated by Django 3.1.5 on 2021-01-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20210104_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('1', 'hr'), ('2', 'user'), ('3', 'admin')], default='2', max_length=1),
        ),
    ]
