# Generated by Django 2.2.3 on 2019-07-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190723_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]