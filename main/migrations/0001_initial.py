# Generated by Django 5.2.4 on 2025-07-04 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('student_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер студента')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_submitted', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Формы обратной связи',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('student_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер студента')),
                ('role', models.CharField(choices=[('user', 'Пользователь'), ('administrator', 'Администратор')], default='user', max_length=20, verbose_name='Роль')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название работы')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('short_description', models.CharField(max_length=300, verbose_name='Краткое описание')),
                ('long_description', models.TextField(verbose_name='Полное описание')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Лайки')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Научная работа',
                'verbose_name_plural': 'Научные работы',
            },
        ),
    ]
