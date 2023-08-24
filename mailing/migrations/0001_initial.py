# Generated by Django 4.2.3 on 2023-07-07 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время начала рассылки (ч:м:с)')),
                ('frequency', models.CharField(choices=[('DA', 'Once a day'), ('WE', 'Once a week'), ('MO', 'Once a month')], default='DA', max_length=2, verbose_name='Периодичность рассылки')),
                ('status', models.CharField(choices=[('CM', 'Completed'), ('CR', 'Created'), ('LA', 'Launched')], default='CR', max_length=2, verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(blank=True, to='mailing.client', verbose_name='Клиенты')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Тема')),
                ('body', models.TextField(default=None, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=255, unique_for_date='created', verbose_name='Слаг')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(upload_to='blog/', verbose_name='Изображение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('published', models.BooleanField(default=False, verbose_name='Признак публикации')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('AC', 'Active'), ('CO', 'Completed')], default='AC', max_length=2, verbose_name='Статус попытки рассылки')),
                ('server_request', models.CharField(max_length=250)),
                ('mailing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.mailing')),
            ],
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='Сообщение'),
        ),
    ]
