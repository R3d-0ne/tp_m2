import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

csv_file_path = BASE_DIR / 'data' / 'Marketing.csv'
mongo_uri = 'mongodb://localhost:27017'  # URI MongoDB (ici pour une instance locale)
db_name = 'concessionnaire'  # Nom de la base de données
collection_name = 'marketing'  # Nom de la collection où les données seront insérées

def import_csv_to_mongo(uri, db_name, collection_name, file_path):
    command = [
        "mongoimport",
        "--uri", uri,
        "--db", db_name,
        "--collection", collection_name,
        "--type", "csv",
        "--headerline",
        "--file", file_path
    ]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Importation réussie :", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'importation :", e.stderr)


import_csv_to_mongo(
    uri="mongodb://localhost:27016",
    db_name="concessionnaire",
    collection_name="marketing",
    file_path=csv_file_path
)
