**Tutorial Paso a Paso sobre Redes y Sockets en Python para Dos Máquinas (Windows)**

Este tutorial te guiará para configurar un servidor y un cliente en dos máquinas Windows diferentes, utilizando sockets TCP en Python.

**Requisitos:**

  * Dos computadoras con Windows conectadas a la misma red local (por ejemplo, la misma red Wi-Fi o Ethernet).
  * Python instalado en ambas máquinas.

**Pasos:**

**1. Obtener la Dirección IP de la Máquina Servidora:**

En la máquina que actuará como **servidor**, sigue estos pasos para encontrar su dirección IP local:

1.  Abre el **Símbolo del sistema** (busca "cmd" en el menú Inicio).
2.  Escribe el comando `ipconfig` y presiona Enter.
3.  Busca la sección correspondiente a tu conexión de red (Ethernet o Wi-Fi).
4.  Anota el valor que aparece junto a "**Dirección IPv4**". Esta es la dirección IP que el cliente necesitará para conectarse. Por ejemplo: `192.168.1.105`.

**2. Código del Servidor (server.py):**

Guarda este código en un archivo llamado `server.py` en la máquina que actuará como servidor:

```python
import socket

# Obtén la dirección IP de la máquina (esto podría no ser necesario en todos los casos,
# pero ayuda a asegurar que el servidor escuche en todas las interfaces)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Define el puerto en el que el servidor escuchará
PORT = 12345  # Elige un puerto que no esté en uso

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección IP y al puerto
server_address = (local_ip, PORT)
server_socket.bind(server_address)
print(f"Servidor escuchando en {local_ip}:{PORT}")

# Escuchar conexiones entrantes (solo se permite una conexión en este ejemplo)
server_socket.listen(1)

print("Esperando una conexión...")
connection, client_address = server_socket.accept()

try:
    print(f"Conexión establecida con {client_address}")

    while True:
        data = connection.recv(1024)  # Recibir hasta 1024 bytes de datos
        if data:
            print(f"Servidor recibió: {data.decode()}")
            message_to_send = b"Mensaje recibido por el servidor!"
            connection.sendall(message_to_send)
        else:
            print(f"Conexión cerrada por {client_address}")
            break

finally:
    # Cerrar la conexión
    connection.close()
    server_socket.close()
```

**3. Código del Cliente (client.py):**

Guarda este código en un archivo llamado `client.py` en la **otra** máquina Windows (la que actuará como cliente). **Reemplaza `'DIRECCION_IP_DEL_SERVIDOR'` con la dirección IP que obtuviste en el paso 1.**

```python
import socket

# Dirección IP y puerto del servidor
SERVER_IP = 'DIRECCION_IP_DEL_SERVIDOR'  # <--- ¡Reemplaza esto!
PORT = 12345

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectar al servidor
    server_address = (SERVER_IP, PORT)
    print(f"Conectando a {SERVER_IP}:{PORT}")
    client_socket.connect(server_address)
    print("Conexión establecida con el servidor.")

    # Enviar un mensaje al servidor
    message = b"Hola desde el cliente!"
    print(f"Cliente enviando: {message.decode()}")
    client_socket.sendall(message)

    # Recibir la respuesta del servidor
    data = client_socket.recv(1024)
    print(f"Cliente recibió: {data.decode()}")

finally:
    print("Cerrando conexión del cliente.")
    client_socket.close()
```

**4. Ejecución:**

1.  **En la máquina que configuraste como servidor:**

      * Abre el **Símbolo del sistema**.
      * Navega hasta el directorio donde guardaste `server.py` usando el comando `cd`.
      * Ejecuta el servidor con el comando: `python server.py`
      * Deberías ver un mensaje indicando que el servidor está escuchando en la dirección IP y el puerto.

2.  **En la máquina que configuraste como cliente:**

      * Abre otro **Símbolo del sistema**.
      * Navega hasta el directorio donde guardaste `client.py` usando el comando `cd`.
      * Ejecuta el cliente con el comando: `python client.py`
      * Deberías ver mensajes indicando que el cliente se está conectando al servidor y luego la respuesta del servidor.

**Explicación de los Cambios:**

  * **Obtención de la IP del Servidor:** Ahora se enfatiza la necesidad de obtener la dirección IP de la máquina donde correrá el servidor.
  * **Enlace del Servidor:** En el código del servidor, se utiliza `socket.gethostname()` y `socket.gethostbyname()` para intentar obtener la dirección IP local de la máquina. Esto asegura que el servidor escuche en la interfaz de red correcta. También se introduce una variable `PORT` para facilitar el cambio del puerto.
  * **Conexión del Cliente:** En el código del cliente, la variable `SERVER_IP` debe ser **reemplazada** con la dirección IP real de la máquina servidora.
  * **Mensajes:** Se han añadido mensajes más descriptivos para que cada uno sepa qué está haciendo su programa.
  * **Tamaño de Recepción:** Se especifica un tamaño máximo de recepción (`1024` bytes) para evitar problemas con mensajes largos.
  * **Cierre de Sockets:** Se asegura que ambos sockets (cliente y servidor) se cierren correctamente en los bloques `finally`.

**Consideraciones Importantes:**

  * **Firewall de Windows:** Es posible que el Firewall de Windows en la máquina servidora bloquee las conexiones entrantes al puerto que elegiste (en este caso, el 12345). Si el cliente no puede conectarse, deberás crear una **regla de entrada** en el Firewall de Windows para permitir las conexiones TCP al puerto 12345.
  * **Red Local:** Asegúrate de que ambas máquinas estén en la misma red local y puedan comunicarse entre sí. Puedes intentar hacer un "ping" desde una máquina a la otra usando la dirección IP para verificar la conectividad básica.
  * **Puerto:** Elige un número de puerto alto (mayor que 1023) para evitar conflictos con servicios del sistema. Asegúrate de usar el mismo puerto tanto en el servidor como en el cliente.


**verificación de escucha**

    netstat -an | findstr "LISTENING"