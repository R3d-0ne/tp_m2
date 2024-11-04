from hdfs import InsecureClient
import pandas as pd

# Configuration du client HDFS
HDFS_HOST = 'http://namenode:9870'  # URL de NameNode
HDFS_USER = 'root'  # Nom de l'utilisateur HDFS

# Initialisation du client HDFS
client = InsecureClient(HDFS_HOST, user=HDFS_USER)

# Dictionnaire des chemins de fichiers
files_to_upload = {
    'data/CO2.csv': '/data_lake/raw/CO2/CO2.csv',
    'data/Clients_18.csv': '/data_lake/raw/clients/Clients_18.csv',
    'data/Immatriculations.csv': '/data_lake/raw/immatriculations/Immatriculations.csv',
    'data/Marketing.csv': '/data_lake/raw/marketing/Marketing.csv'
}

def upload_file_to_hdfs(local_path, hdfs_path):
    """Fonction pour uploader un fichier local vers HDFS."""
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
    """Lecture d'un fichier CSV depuis HDFS et affichage des données."""
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
    for local_file, hdfs_file in files_to_upload.items():
        upload_file_to_hdfs(local_file, hdfs_file)

    # Lecture et affichage des fichiers
    for _, hdfs_file in files_to_upload.items():
        read_and_display_csv(hdfs_file)

if __name__ == "__main__":
    main()
