# Generated by Django 3.2.3 on 2021-05-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(max_length=500, verbose_name='Текст')),
                ('name', models.CharField(max_length=100, verbose_name='Имя добавившего')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='емаил')),
                ('rating', models.IntegerField(blank=True, default=0, null=True, verbose_name='рейтинг')),
                ('status', models.CharField(choices=[('new', 'новая'), ('moderated', 'модерированная')], default='new', max_length=50, verbose_name='статус')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]