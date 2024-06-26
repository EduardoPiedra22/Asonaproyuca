# Generated by Django 4.2.7 on 2023-11-28 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo_sala', models.CharField(blank=True, choices=[('PRIVADA', 'Privada'), ('PÚBLICA', 'Pública')], max_length=14, null=True)),
            ],
            options={
                'ordering': ('fecha',),
            },
        ),
        migrations.CreateModel(
            name='Usuario_sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.sala')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(blank=True, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('editado', models.BooleanField(default=False)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.sala')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_user_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('fecha',),
            },
        ),
    ]
