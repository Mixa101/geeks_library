# Generated by Django 5.1.3 on 2024-11-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
