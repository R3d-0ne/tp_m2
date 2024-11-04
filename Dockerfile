# Utiliser l'image Hadoop de base
FROM apache/hadoop:3.3.1

# Installer Sqoop
RUN apt-get update && \
    apt-get install -y sqoop && \
    apt-get clean
