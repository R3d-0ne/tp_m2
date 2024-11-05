import requests
import pandas as pd
import json

# Configuration
ORACLE_NOSQL_API_URL = 'http://localhost:8081/v1/sql'


def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS client_data (
        id STRING GENERATED ALWAYS AS UUID,
        age INTEGER,
        sexe STRING,
        taux DOUBLE,
        situationFamiliale STRING,
        nbEnfantsAcharge INTEGER,
        deuxieme_voiture BOOLEAN,
        immatriculation STRING,
        PRIMARY KEY(id)
    )
    """
    try:
        response = requests.post(
            f"{ORACLE_NOSQL_API_URL}",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"statement": create_table_query})
        )

        if response.status_code == 200:
            print("Table 'client_data' créée avec succès.")
        else:
            print(f"Erreur lors de la création de la table : {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la création de la table : {e}")


def push_data_to_oracle(csv_file_path):
    try:
        # Lecture du fichier CSV en spécifiant un encodage approprié
        df = pd.read_csv(csv_file_path, encoding='utf-8')  # Essayez 'latin-1' si 'utf-8' échoue

        # Parcours de chaque ligne du DataFrame
        for _, row in df.iterrows():
            data = {
                "age": int(row['age']),
                "sexe": row['sexe'],
                "taux": float(row['taux']),
                "situationFamiliale": row['situationFamiliale'],
                "nbEnfantsAcharge": int(row['nbEnfantsAcharge']),
                "deuxieme_voiture": bool(row['2eme voiture']),
                "immatriculation": row['immatriculation']
            }

            # Envoi des données au service Oracle NoSQL
            response = requests.post(
                f"{ORACLE_NOSQL_API_URL}/data/client_data",
                headers={"Content-Type": "application/json"},
                data=json.dumps(data)
            )
            if response.status_code == 200:
                print(f"Enregistrement inséré avec succès : {data}")
            else:
                print(f"Erreur lors de l'insertion de l'enregistrement : {response.text}")

    except Exception as e:
        print(f"Erreur lors de l'envoi des données : {e}")
