# Generated by Django 4.0.4 on 2022-05-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_technology_myuser_technology'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'ordering': ['-id'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['name'], 'verbose_name': 'Технология', 'verbose_name_plural': 'Технологии'},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user/avatar/%Y/%m/%d/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='biography',
            field=models.TextField(blank=True, null=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='first_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата подтверждения почты'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=10, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='github',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ссылка на github'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='technology',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='custom_user.technology', verbose_name='Технологии'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
    ]
