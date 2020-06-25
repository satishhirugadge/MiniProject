# Generated by Django 2.1.5 on 2020-06-17 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20200616_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_id', models.UUIDField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Phone_Number', models.IntegerField(max_length=20)),
                ('Email_ID', models.EmailField(max_length=20)),
                ('address1', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectData',
        ),
    ]
