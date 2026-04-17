#!/bin/bash

BUCKET_NAME="devops-bucket-$USER"
FECHA=$(date +%Y-%m-%d_%H-%M-%S)
ARCHIVO_LOG="backup_$FECHA.log"

echo "=========================================="
echo "  Script de Respaldo Automatizado"
echo "=========================================="
echo "Fecha: $FECHA"
echo "Bucket destino: $BUCKET_NAME"
echo ""

# Crear archivo de log simulado
echo "Iniciando respaldo..." > $ARCHIVO_LOG
echo "Fecha: $FECHA" >> $ARCHIVO_LOG
echo "Archivos respaldados:" >> $ARCHIVO_LOG
ls -la >> $ARCHIVO_LOG
echo "Respaldo completado." >> $ARCHIVO_LOG

echo "[OK] Archivo de log creado: $ARCHIVO_LOG"
echo "[INFO] En EC2 este script subirá el log a S3 con:"
echo "       aws s3 cp $ARCHIVO_LOG s3://$BUCKET_NAME/"
echo ""
echo "=========================================="
echo "  Proceso finalizado exitosamente"
echo "=========================================="