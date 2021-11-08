# Generated by Django 3.2.9 on 2021-11-08 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_posts_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Question', models.CharField(max_length=100)),
                ('Option1', models.CharField(max_length=100)),
                ('Option2', models.CharField(max_length=100)),
                ('Option3', models.CharField(max_length=100)),
                ('Option4', models.CharField(max_length=100)),
                ('Corrans', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
