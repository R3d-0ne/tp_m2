from hdfs import InsecureClient
import pandas as pd

# Configuration du client HDFS
HDFS_HOST = 'http://localhost:9870'  # URL de NameNode
HDFS_USER = 'root'  # Nom de l'utilisateur HDFS

# Initialisation du client HDFS
client = InsecureClient(HDFS_HOST, user=HDFS_USER)

# Dictionnaire des chemins de fichiers
files_to_upload = {
    'data/CO2.csv': '/data_lake/raw/CO2/CO2.csv',
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

def read_and_display_csv(hdfs_path):
    """Lit un fichier CSV depuis HDFS et affiche les premières lignes ainsi que des statistiques."""
    try:
        with client.read(hdfs_path, encoding='utf-8') as reader:
            df = pd.read_csv(reader)
            print(f"Aperçu des données de {hdfs_path} :")
            print(df.head())
            print("\nStatistiques descriptives :")
            print(df.describe())
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {hdfs_path} : {e}")

def main():
    """Fonction principale pour gérer le téléchargement et l'affichage des fichiers."""
    for local_file, hdfs_file in files_to_upload.items():
        upload_file_to_hdfs(local_file, hdfs_file)

    # Lecture et affichage des fichiers
    for _, hdfs_file in files_to_upload.items():
        read_and_display_csv(hdfs_file)

