# Generated by Django 3.1.4 on 2021-01-07 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_category_comment_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='jum',
            field=models.IntegerField(default=0),
        ),
    ]