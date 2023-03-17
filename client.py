import socket
import socket
import os

HOST = '127.0.0.1' # Adresse IP du serveur
PORT = 65432 # Port d'écoute du serveur

# Établir une connexion avec le serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Envoyer des requêtes au serveur jusqu'à ce que l'utilisateur entre "QUIT"
    while True:
        command = input('taper LIST pour voir les fichier,download <nom_du_fichier.extension> pour télécharger ou QUITTER pour vous deconnecter:').strip().upper()
        if command == 'QUITTER':
            client_socket.sendall(command.encode("utf-8"))
            break
        elif command == 'LIST':
            # Demander la liste des fichiers hébergés
            client_socket.sendall(command.encode("utf-8"))

            # Récupérer la réponse du serveur et afficher la liste des fichiers
            data = client_socket.recv(1024).decode("ISO-8859-1")
            file_list = data.split()
            print(f'fichier sur le server: {", ".join(file_list)}')
        elif command.startswith('DOWNLOAD'):
            # Demander le contenu des fichiers spécifiés
            client_socket.sendall(command.encode("utf-8"))

            # Récupérer le contenu des fichiers et les sauvegarder localement
            response_data = b''
            for file_name in command.split()[1:]:
                file_content = client_socket.recv(1024)
                response_data += file_content

                # Sauvegarder le contenu dans un fichier local
                with open(os.path.join('fichier_client', file_name), 'wb') as file:

                    file.write(file_content)

            print(f'fichier télécharger: {", ".join(command.split()[1:])}')
        else:
            print('commande inconnue')
