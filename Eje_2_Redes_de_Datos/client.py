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
