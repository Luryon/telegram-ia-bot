import redis
from dotenv import load_dotenv
import os
import ssl



def main():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()
    # Configuración de conexión a Valkey en AWS ElastiCache
    valkey_host = os.environ["VALKEY_HOST"]
    valkey_port = os.environ["VALKEY_PORT"]

    # Conectar (sin autenticación, si la configuraste en AWS, añade el password)
    valkey_client = redis.Redis(
        host=valkey_host,
        port=valkey_port,
        password=None,  # Agregar si configuraste autenticación en AWS
        decode_responses=True,
        ssl=True,
        ssl_cert_reqs=ssl.CERT_NONE,
    )

    valkey_client.ping() 

    print('connected to redis "{}"'.format(valkey_client)) 

    # Prueba guardando un valor
    valkey_client.set("mensaje", "¡Hola desde Valkey en AWS!")

    # Recuperar el valor
    mensaje = valkey_client.get("mensaje")
    print(f"Mensaje desde Valkey: {mensaje}")


main()