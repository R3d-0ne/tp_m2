import requests
import pandas as pd
import json

# Configuration



ORACLE_NOSQL_API_URL = 'http://localhost:808O'
ADMIN_USERNAME = 'R3d-0ne'  # Remplacez par votre nom d'utilisateur Oracle NoSQL

# Fonction pour s'authentifier et obtenir un token
def authenticate():
    """
    Authentifie auprès du service Oracle NoSQL et retourne le token.
    """
    try:
        response = requests.post(
            'http://localhost:8080/V0/nosql/admin/login',  # Assurez-vous que le port et l'URL sont corrects
            headers={"Content-Type": "application/json"},
            json={"user": "admin", "password": "password"}
        )
        print(response.text)


        if response.status_code == 200:
            token = response.json().get('token')
            print("Authentification réussie.")
            return token
        else:
            print(f"Erreur lors de l'authentification : {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'authentification : {e}")
        return None


def create_table(token):
    """
    Crée une table dans Oracle NoSQL correspondant aux colonnes du fichier CSV.
    """
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
            f"{ORACLE_NOSQL_API_URL}/sql",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            },
            data=json.dumps({"statement": create_table_query})
        )

        if response.status_code == 200:
            print("Table 'client_data' créée avec succès.")
        else:
            print(f"Erreur lors de la création de la table : {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la création de la table : {e}")


def push_data_to_oracle(csv_file_path, token):
    """
    Pousse les données CSV vers la table Oracle NoSQL.
    """
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
                f"{ORACLE_NOSQL_API_URL}/kvstore/client_data",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}"
                },
                data=json.dumps(data)
            )
            if response.status_code == 200:
                print(f"Enregistrement inséré avec succès : {data}")
            else:
                print(f"Erreur lors de l'insertion de l'enregistrement : {response.text}")

    except Exception as e:
        print(f"Erreur lors de l'envoi des données : {e}")


if __name__ == "__main__":
    # Étape 1 : Authentification
    token = authenticate()

    if token:
        # Étape 2 : Créer la table dans Oracle NoSQL
        create_table(token)

        # Étape 3 : Pousser les données CSV vers Oracle NoSQL
        push_data_to_oracle('data/Clients_0.csv', token)
