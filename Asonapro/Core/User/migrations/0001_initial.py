# Generated by Django 5.0.6 on 2024-05-31 15:02

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='users1/%Y/%m/%d')),
                ('token', models.UUIDField(blank=True, editable=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Sembradores',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cedula', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cédula')),
                ('cedula_agraria', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cédula Agraria')),
                ('codigo_asonaproyuca', models.CharField(blank=True, max_length=100, null=True, verbose_name='Código Asonaproyuca')),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('telefono_personal', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono Personal')),
                ('telefono_casa', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono de Casa')),
                ('direccion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('edad', models.IntegerField(blank=True, null=True, verbose_name='Edad')),
                ('estado_civil', models.CharField(choices=[('soltero', 'Soltero(a)'), ('casado', 'Casado(a)'), ('divorciado', 'Divorciado(a)'), ('viudo', 'Viudo(a)')], max_length=30, verbose_name='Estado Civil')),
                ('profesion_ocupacion', models.CharField(blank=True, max_length=20, null=True, verbose_name='Profesión u Ocupación')),
                ('sexo', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], max_length=10, null=True, verbose_name='Sexo')),
                ('logue_complete', models.BooleanField(default=False, verbose_name='Registro Completo')),
                ('estado', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado')),
                ('municipio', models.CharField(blank=True, max_length=50, null=True, verbose_name='Municipio')),
                ('parroquia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Parroquia')),
                ('nombre_unidad', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre de la Unidad')),
                ('conyuge_nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del Cónyuge')),
                ('conyuge_apellido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido del Cónyuge')),
                ('conyuge_cedula', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Cédula del Cónyuge')),
                ('conyuge_edad', models.IntegerField(blank=True, null=True, verbose_name='Edad del Cónyuge')),
                ('conyuge_sexo', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], max_length=10, null=True, verbose_name='Sexo del Cónyuge')),
                ('conyuge_telefono_fijo', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono Fijo del Cónyuge')),
                ('conyuge_telefono_celular', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono Celular del Cónyuge')),
                ('direccion_habitacion_estado', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado de la Dirección de Habitación')),
                ('direccion_habitacion_municipio', models.CharField(blank=True, max_length=50, null=True, verbose_name='Municipio de la Dirección de Habitación')),
                ('direccion_habitacion_parroquia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Parroquia de la Dirección de Habitación')),
                ('direccion_habitacion_caserio', models.CharField(blank=True, max_length=50, null=True, verbose_name='Caserío de la Dirección de Habitación')),
                ('direccion_habitacion_sector', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sector de la Dirección de Habitación')),
                ('direccion_habitacion_ciudad_cercana', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ciudad Cercana de la Dirección de Habitación')),
                ('direccion_habitacion_punto_referencia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Punto de Referencia de la Dirección de Habitación')),
                ('direccion_habitacion_direccion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección de Habitación')),
            ],
            options={
                'verbose_name': 'Sembrador',
                'verbose_name_plural': 'Sembradores',
            },
            bases=('User.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cedula', models.CharField(blank=True, max_length=20, null=True)),
                ('estado', models.CharField(max_length=100, null=True)),
                ('oficina', models.CharField(blank=True, max_length=100, null=True)),
                ('profesion', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('logue_complete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Tecnicos',
            },
            bases=('User.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
