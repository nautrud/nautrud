# Generated by Django 5.2.4 on 2025-07-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='tags',
            field=models.CharField(blank=True, help_text='Введите теги через запятую (например: математика, физика, исследование)', max_length=500, null=True, verbose_name='Теги/Категории'),
        ),
    ]
