import boto3
import os
from datetime import datetime

# --- CONFIGURACIÓN ---
# 1. Asegúrate de que este nombre sea IGUAL al que creaste en la consola de AWS S3
# 2. Quita cualquier espacio extra al final
BUCKET_NAME = "avance-devops-bucket" 
REGION = "us-east-1"

def listar_buckets():
    print("==========================================")
    print("   Buckets S3 disponibles en tu cuenta")
    print("==========================================")
    s3 = boto3.client("s3", region_name=REGION)
    respuesta = s3.list_buckets()
    buckets = respuesta.get("Buckets", [])
    if buckets:
        for bucket in buckets:
            print(f"  - {bucket['Name']} (creado: {bucket['CreationDate'].strftime('%Y-%m-%d')})")
    else:
        print("  No se encontraron buckets.")
    print("")

def subir_archivo(ruta_local, nombre_destino):
    print(f"Subiendo '{ruta_local}' a s3://{BUCKET_NAME}/backups/{nombre_destino} ...")
    s3 = boto3.client("s3", region_name=REGION)
    # Aquí subimos el archivo
    s3.upload_file(ruta_local, BUCKET_NAME, f"backups/{nombre_destino}")
    print(f"[OK] Archivo subido exitosamente.")
    print("")

def listar_archivos_bucket():
    print(f"Archivos en s3://{BUCKET_NAME}/backups/")
    print("------------------------------------------")
    s3 = boto3.client("s3", region_name=REGION)
    # Prefix ayuda a listar solo lo que está en la carpeta 'backups/'
    respuesta = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix="backups/")
    archivos = respuesta.get("Contents", [])
    if archivos:
        for archivo in archivos:
            tamano_kb = round(archivo['Size'] / 1024, 2)
            print(f"  - {archivo['Key']} ({tamano_kb} KB)")
    else:
        print("  La carpeta backups/ esta vacia.")
    print("")

def crear_reporte():
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"reporte_{fecha}.txt"
    
    # Crea la carpeta 'scripts' si no existe para evitar errores
    if not os.path.exists("scripts"):
        os.makedirs("scripts")
        
    ruta_local = f"scripts/{nombre_archivo}"

    with open(ruta_local, "w") as f:
        f.write("==========================================\n")
        f.write("   Reporte Automatizado - DevOps Project\n")
        f.write("==========================================\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Bucket: {BUCKET_NAME}\n")
        f.write(f"Region: {REGION}\n")
        f.write("Estado: Operacional\n")
        f.write("==========================================\n")

    print(f"[OK] Reporte creado localmente: {ruta_local}")
    return ruta_local, nombre_archivo

# --- Ejecucion principal ---
if __name__ == "__main__":
    print("")
    print("==========================================")
    print("   S3 Manager con Boto3")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("==========================================")
    print("")

    try:
        listar_buckets()
        ruta, nombre = crear_reporte()
        subir_archivo(ruta, nombre)
        listar_archivos_bucket()
    except Exception as e:
        print(f"Error detectado: {e}")

    print("==========================================")
    print("   Script finalizado")
    print("==========================================")