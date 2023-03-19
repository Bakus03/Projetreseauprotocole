# Projetreseauprotocole
Client server 
1)	Exécution du serveur
Ouvrir un terminal
Aller dans le répertoire où se trouve le fichier server.py
Entrer la commande python server.py
Le serveur devrait maintenant être en écoute sur l'adresse IP et le numéro de port spécifiés.

2)	Utilisation des clients
Ouvrir un terminal
Entrer la commande telnet <adresse_IP> <numéro_de_port>pour se connecter au serveur
Si la connexion est établie, la liste des fichiers hébergés sur le serveur sera affichée dans le terminal du client.
Pour télécharger un fichier, entrer la commande DOWNLOAD <nom_du_fichier>dans le terminal du client.
Si le fichier existe sur le serveur, il sera téléchargé dans le répertoire courant du client.
Si le fichier n'existe pas sur le serveur, un message d'erreur sera affiché dans le terminal du client.
Pour terminer la session, entrer la commande QUIT dans le terminal du client.
