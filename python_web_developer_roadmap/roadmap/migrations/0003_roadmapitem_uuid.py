# Generated by Django 3.2.16 on 2022-10-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0002_auto_20221010_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadmapitem',
            name='uuid',
            field=models.UUIDField(default='6ada4aba-9b49-487a-8806-e1da422ab8fe'),
            preserve_default=False,
        ),
    ]