import pandas as pd
from hdfs import InsecureClient

# Configuration du client HDFS
HDFS_HOST = 'http://localhost:50070'
HDFS_USER = 'root'  # Nom de l'utilisateur HDFS

# Initialisation du client HDFS
client = InsecureClient(HDFS_HOST, user=HDFS_USER)

# Dictionnaire des chemins de fichiers
files_to_upload = {
    'data/Clients_0.csv': '/data_lake/raw/Clients/Clients_0.csv',
}

def upload_file_to_hdfs(local_path, hdfs_path):
    """Télécharge un fichier local vers HDFS s'il n'existe pas déjà."""
    try:
        if not client.status(hdfs_path, strict=False):
            print(f"Téléchargement du fichier {local_path} vers {hdfs_path} sur HDFS...")
            client.upload(hdfs_path, local_path)
            print("Téléchargement terminé avec succès.")
        else:
            print(f"Le fichier {hdfs_path} existe déjà sur HDFS.")
    except Exception as e:
        print(f"Erreur lors du téléchargement du fichier {local_path} : {e}")

def main():
    """Fonction principale pour gérer le téléchargement des fichiers sur HDFS."""
    for local_file, hdfs_file in files_to_upload.items():
        upload_file_to_hdfs(local_file, hdfs_file)

