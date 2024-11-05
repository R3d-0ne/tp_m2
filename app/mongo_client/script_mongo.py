import pandas as pd
from pymongo import MongoClient
import pandas as pd
from hdfs import InsecureClient

csv_file_path = '../../data/Marketing.csv'  # Remplace par le chemin de ton fichier CSV

import pandas as pd

with open(csv_file_path, mode='r') as file:
    contenu = file.read()
    print(contenu)





# Paramètres
mongo_uri = 'mongodb://localhost:27017'  # URI MongoDB (ici pour une instance locale)
db_name = 'concessionnaire'  # Nom de la base de données
collection_name = 'marketing'  # Nom de la collection où les données seront insérées




df = pd.read_csv(csv_file_path)

print
# print(df)

# # 2. Connexion à MongoDB
# client = MongoClient(mongo_uri)
# db = client[db_name]
# collection = db[collection_name]

# # 3. Transformer le DataFrame en dictionnaires et insérer dans MongoDB
# data_dict = df.to_dict("records")  # Convertir le DataFrame en une liste de dictionnaires
# collection.insert_many(data_dict)   # Insérer les données dans MongoDB

# print("Données insérées dans MongoDB avec succès!")
