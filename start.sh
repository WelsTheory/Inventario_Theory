#!/bin/bash
# Inventario Theory — puerto 3001

echo "Iniciando Inventario Theory..."
echo "================================"

cd "$(dirname "${BASH_SOURCE[0]}")"

# Activar entorno virtual si existe, si no usa Python del sistema
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
    echo "✓ Entorno virtual activado"
else
    echo "✓ Usando Python del sistema (sin venv)"
fi

# Cargar variables de entorno
if [ -f .env ]; then
    set -a
    source .env
    set +a
    echo "✓ Variables de entorno cargadas"
else
    echo "ERROR: Archivo .env no encontrado. Copia .env.example como .env y configúralo."
    exit 1
fi

# Instalar/actualizar dependencias
echo ""
echo "Verificando dependencias..."
pip3 install -r requirements.txt --quiet
echo "✓ Dependencias OK"

# Aplicar migraciones
echo ""
echo "Aplicando migraciones..."
python3 manage.py migrate --run-syncdb
if [ $? -ne 0 ]; then
    echo "ERROR: Falló la migración"
    exit 1
fi
echo "✓ Base de datos lista"

# IP de Tailscale
TAILSCALE_IP=$(ip addr show tailscale0 2>/dev/null | grep "inet " | awk '{print $2}' | cut -d/ -f1)

echo ""
echo "================================"
echo "Inventario Theory corriendo en:"
echo "  Local:    http://localhost:3001"
if [ -n "$TAILSCALE_IP" ]; then
    echo "  Tailscale: http://$TAILSCALE_IP:3001"
fi
echo ""
echo "Ctrl+C para detener"
echo "================================"
echo ""

python3 manage.py runserver 0.0.0.0:3001
