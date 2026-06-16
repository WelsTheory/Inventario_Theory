from django.db import models


class Componente(models.Model):
    CATEGORIA_CHOICES = [
        ('resistencia', 'Resistencia'),
        ('capacitor', 'Capacitor'),
        ('led', 'LED'),
        ('transistor', 'Transistor'),
        ('diodo', 'Diodo'),
        ('inductor', 'Inductor'),
        ('sensor', 'Sensor'),
        ('display', 'Display'),
        ('modulo', 'Módulo'),
        ('conector', 'Conector'),
        ('cable', 'Cable'),
        ('herramienta', 'Herramienta'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=150)
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES, default='otro')
    valor = models.CharField(max_length=50, blank=True, help_text="Ej: 10kΩ, 100µF, 5V")
    cantidad = models.PositiveIntegerField(default=1)
    ubicacion = models.CharField(max_length=200, help_text="Ej: Caja roja, Bandeja 3")
    notas = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        ordering = ['categoria', 'nombre']

    def __str__(self):
        if self.valor:
            return f"{self.nombre} {self.valor}"
        return self.nombre
