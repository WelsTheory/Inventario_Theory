from django.db import models


class Placa(models.Model):
    TIPO_CHOICES = [
        ('microcontrolador', 'Microcontrolador'),
        ('placa', 'Placa de desarrollo'),
        ('modulo', 'Módulo'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES, default='placa')
    descripcion = models.TextField(blank=True)
    ubicacion_fisica = models.CharField(max_length=200, blank=True, help_text="Ej: Cajón 2, Caja azul")
    directorio_pc = models.CharField(max_length=500, blank=True, help_text="Ruta en el PC")
    repo_url = models.URLField(blank=True, verbose_name="Repositorio")
    imagen = models.ImageField(upload_to='placas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa'
        verbose_name_plural = 'Placas'
        ordering = ['nombre']

    @property
    def estado_cursos(self):
        videos = list(self.videos.all())
        if not videos:
            return None
        if any(not v.finalizado for v in videos):
            return 'en_curso'
        return 'finalizado'

    def __str__(self):
        return self.nombre


class Video(models.Model):
    placa = models.ForeignKey(Placa, on_delete=models.CASCADE, related_name='videos')
    titulo = models.CharField(max_length=200)
    url = models.URLField()
    descripcion = models.CharField(max_length=300, blank=True)
    finalizado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.titulo
