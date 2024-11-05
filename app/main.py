from hdfs_client.script_hdfs import main as hdfs_main
from oracle_client.script_oracle import create_table, push_data_to_oracle

if __name__ == "__main__":
    create_table()  # Crée la table dans Oracle NoSQL avant d'importer les données
    hdfs_main()  # Exécute le script de HDFS pour télécharger les fichiers sur HDFS
    push_data_to_oracle('data/Clients_0.csv')  # Pousse les données du fichier CSV vers Oracle NoSQL
