# Inventario Theory

Aplicación web local para inventariar **placas de desarrollo electrónicas** (Arduino, ESP32, Raspberry Pi, etc.) y **componentes electrónicos** (resistencias, capacitores, sensores, etc.).

Construida con Django 5 y una UI dark mode basada en Bootstrap 5.

---

## Caracteristicas

- **Placas**: registra nombre, tipo, ubicacion fisica, directorio en PC, repositorio y videos de referencia
- **Componentes**: registra nombre, categoria, valor, cantidad y ubicacion en el taller
- **Busqueda y filtros** en ambos modulos
- **Imagenes**: sube fotos de tus placas
- **Admin de Django** disponible en `/admin/`
- **Acceso por Tailscale** detectado automaticamente al iniciar

---

## Requisitos

- Python 3.10+
- pip

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repo>
cd inventario_electronico
```

### 2. Crear entorno virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copia el archivo de ejemplo y edítalo:

```bash
cp .env.example .env
```

Genera una `SECRET_KEY` segura:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Pega el resultado en `.env`:

```env
SECRET_KEY='tu-clave-generada-aqui'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

> Si accedes desde otro dispositivo vía Tailscale, agrega tu IP de Tailscale:
> `ALLOWED_HOSTS=localhost,127.0.0.1,100.x.x.x`

### 5. Crear la base de datos

```bash
python3 manage.py migrate
```

### 6. (Opcional) Crear superusuario para el admin de Django

```bash
python3 manage.py createsuperuser
```

---

## Uso

### Arranque rápido con el script incluido

```bash
bash start.sh
```

El script activa el entorno virtual (si existe), carga el `.env`, instala/actualiza dependencias, aplica migraciones y levanta el servidor.

### O arranque manual

```bash
source venv/bin/activate
python3 manage.py runserver 0.0.0.0:3001
```

Abre en el navegador: [http://localhost:3001](http://localhost:3001)

---

## Estructura del proyecto

```
inventario_electronico/
├── config/          # Configuración Django (settings, urls, wsgi)
├── core/            # Dashboard y página de agregado rápido
├── placas/          # Módulo de placas y microcontroladores
├── componentes/     # Módulo de componentes electrónicos
├── templates/       # Plantillas HTML
├── .env.example     # Plantilla de variables de entorno
├── requirements.txt
└── start.sh         # Script de arranque
```

---

## Módulos

### Placas

Registra placas de desarrollo y microcontroladores con:

- Nombre, tipo (microcontrolador / placa / módulo / otro)
- Descripción, ubicación física y directorio en el PC
- URL del repositorio
- Estado del curso (finalizado / en curso)
- Imagen y videos asociados

### Componentes

Registra componentes electrónicos con:

- Nombre, categoría (resistencia, capacitor, LED, sensor, etc.)
- Valor (ej: 10kΩ, 100µF), cantidad y ubicación física
- Notas adicionales

---

## Admin de Django

Disponible en [http://localhost:3001/admin](http://localhost:3001/admin) (requiere superusuario).

---

## Acceso por red local / Tailscale

El servidor escucha en `0.0.0.0:3001`, por lo que es accesible desde cualquier dispositivo en la misma red o conectado vía Tailscale. Solo asegúrate de agregar la IP al `ALLOWED_HOSTS` en el `.env`.
