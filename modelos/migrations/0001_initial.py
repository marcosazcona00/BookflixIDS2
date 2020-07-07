# Generated by Django 3.0.5 on 2020-07-07 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.IntegerField(default=0)),
                ('fecha_calificacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35, unique=True)),
            ],
            options={
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editoriales',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('foto', models.FileField(blank=True, null=True, upload_to='')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('esta_completo', models.BooleanField(default=0)),
                ('fecha_lanzamiento', models.DateTimeField(null=True)),
                ('fecha_vencimiento', models.DateTimeField(null=True)),
                ('autor', models.ForeignKey(max_length=35, on_delete=django.db.models.deletion.CASCADE, to='modelos.Autor')),
                ('editorial', models.ForeignKey(max_length=35, on_delete=django.db.models.deletion.CASCADE, to='modelos.Editorial')),
                ('genero', models.ForeignKey(max_length=25, on_delete=django.db.models.deletion.CASCADE, to='modelos.Genero')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Novedad',
                'verbose_name_plural': 'Novedades',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_tarjeta', models.CharField(max_length=16)),
                ('fecha_vencimiento', models.DateField()),
                ('empresa', models.CharField(max_length=254)),
                ('codigo_seguridad', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Suscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_maxima_perfiles', models.IntegerField(default=0)),
                ('tipo_suscripcion', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default=None, max_length=255, unique=True)),
                ('descripcion', models.TextField()),
                ('pdf', models.FileField(blank=True, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('libro_asociado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelos.Libro')),
            ],
            options={
                'verbose_name': 'Trailer',
                'verbose_name_plural': 'Trailers',
            },
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('auth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fecha_suscripcion', models.DateField()),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('nro_tarjeta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modelos.Tarjeta')),
                ('tipo_suscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Tipo_Suscripcion')),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_perfil', models.CharField(max_length=25)),
                ('foto', models.FileField(blank=True, null=True, upload_to='')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Suscriptor')),
                ('listado_favoritos', models.ManyToManyField(to='modelos.Libro')),
            ],
            options={
                'unique_together': {('nombre_perfil', 'auth')},
            },
        ),
        migrations.CreateModel(
            name='Libro_Incompleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esta_completo', models.BooleanField(default=0, null=True)),
                ('libro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modelos.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Libro_Completo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo_pdf', models.FileField(upload_to='')),
                ('libro', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='modelos.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('spoiler', models.BooleanField(default=0)),
                ('spoiler_admin', models.BooleanField(default=0)),
                ('calificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Calificacion', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capitulo', models.IntegerField()),
                ('fecha_lanzamiento', models.DateTimeField()),
                ('fecha_vencimiento', models.DateTimeField(null=True)),
                ('archivo_pdf', models.FileField(upload_to='')),
                ('ultimo', models.BooleanField(default=0, null=True)),
                ('titulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Libro_Incompleto')),
            ],
            options={
                'unique_together': {('capitulo', 'titulo')},
            },
        ),
        migrations.AddField(
            model_name='calificacion',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Libro'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelos.Perfil'),
        ),
        migrations.CreateModel(
            name='Lee_libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminado', models.NullBooleanField()),
                ('ultimo_acceso', models.DateTimeField(null=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Libro')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Perfil')),
            ],
            options={
                'unique_together': {('libro', 'perfil')},
            },
        ),
        migrations.CreateModel(
            name='Lee_Capitulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultimo_acceso', models.DateTimeField(null=True)),
                ('capitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Capitulo')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Perfil')),
            ],
            options={
                'unique_together': {('capitulo', 'perfil')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='calificacion',
            unique_together={('libro', 'perfil')},
        ),
    ]
