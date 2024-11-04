#!/bin/bash

# Créer les répertoires HDFS
hdfs dfs -mkdir -p /data_lake/raw/CO2
hdfs dfs -mkdir -p /data_lake/raw/clients
hdfs dfs -mkdir -p /data_lake/raw/immatriculations
hdfs dfs -mkdir -p /data_lake/raw/marketing
hdfs dfs -mkdir -p /data_lake/processed
hdfs dfs -mkdir -p /data_lake/analytics

# Importer les fichiers dans HDFS
hdfs dfs -put /app/data/CO2.csv /data_lake/raw/CO2/
hdfs dfs -put /app/data/clients.csv /data_lake/raw/clients/
hdfs dfs -put /app/data/immatriculations.csv /data_lake/raw/immatriculations/
hdfs dfs -put /app/data/marketing.csv /data_lake/raw/marketing/

echo "Initialisation HDFS terminée avec succès."
