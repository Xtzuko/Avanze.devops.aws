#!/bin/bash

echo "=========================================="
echo "  Verificacion del entorno DevOps"
echo "=========================================="

# Verificar Git
if command -v git &> /dev/null; then
    echo "[OK] Git instalado: $(git --version)"
else
    echo "[ERROR] Git no encontrado"
fi

# Verificar Python
if command -v python3 &> /dev/null; then
    echo "[OK] Python instalado: $(python3 --version)"
else
    echo "[ERROR] Python3 no encontrado"
fi

# Verificar pip
if command -v pip3 &> /dev/null; then
    echo "[OK] pip instalado: $(pip3 --version)"
else
    echo "[ERROR] pip3 no encontrado"
fi

# Verificar AWS CLI
if command -v aws &> /dev/null; then
    echo "[OK] AWS CLI instalado: $(aws --version)"
else
    echo "[AVISO] AWS CLI no encontrado (se usara consola web)"
fi

echo ""
echo "Fecha de ejecucion: $(date)"
echo "Usuario del sistema: $(whoami)"
echo "Directorio actual: $(pwd)"
echo "=========================================="
echo "  Verificacion completada"
echo "=========================================="