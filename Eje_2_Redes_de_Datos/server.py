import socket

# Obtén la dirección IP de la máquina (esto podría no ser necesario en todos los casos,
# pero ayuda a asegurar que el servidor escuche en todas las interfaces)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
#local_ip = '192.168.1.42'
#local_ip = '0.0.0.0'  # Escuchar en todas las interfaces

print(f"Dirección IP local: {local_ip}")

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