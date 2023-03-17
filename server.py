import socket
import os
import threading

HOST = '127.0.0.1' # Adresse IP du serveur
PORT = 65432 # Port d'écoute du serveur
DIRECTORY = r'C:\threading\fichiers'
# Répertoire contenant les fichiers à héberger

# Fonction pour gérer les requêtes des clients
def handle_request(client_socket, client_address):
    print(f'Connection from {client_address}')
    while True:
        # Attendre la requête du client
        data = client_socket.recv(1024).decode("ISO-8859-1")
        if not data:
            break

        # Traiter la requête
        request_parts = data.split()
        command = request_parts[0]

        if command == 'LIST':
            # Renvoyer la liste des fichiers hébergés
            file_list = os.listdir(DIRECTORY)
            response_data = ' '.join(file_list)
            client_socket.sendall(response_data.encode("utf-8"))
        elif command == 'DOWNLOAD':
            # Renvoyer le contenu des fichiers demandés
            for file_name in request_parts[1:]:
                file_path = os.path.join(DIRECTORY, file_name)
                if os.path.exists(file_path) and os.path.isfile(file_path):
                    with open(file_path, 'rb') as file:
                        file_content = file.read()
                        client_socket.sendall(file_content)
        elif command == 'QUIT':
            # Fermer la session
            break

    print(f'Connection from {client_address} closed')
    client_socket.close()

# Lancer le serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f'Server listening on {HOST}:{PORT}')

    while True:
        # Attendre une nouvelle connexion
        client_socket, client_address = server_socket.accept()

        # Traiter la requête du client dans un thread séparé
        client_thread = threading.Thread(target=handle_request, args=(client_socket, client_address))
        client_thread.start()
