import os
import csv
from redis import Redis
from functools import wraps

# Configuration des variables d'environnement
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
APP_PORT = int(os.getenv("APP_PORT", 5000))
ADMIN_KEY = os.getenv("ADMIN_KEY", "default_key")
CSV_FILE_USERS = os.getenv("CSV_FILE", "initial_data_users.csv")
CSV_FILE_QUOTES = os.getenv("CSV_FILE", "initial_data_quotes.csv")

# Connexion à Redis
redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

# Chargement initial des données
if not redis_client.exists("users"):
    if os.path.exists(CSV_FILE_USERS):
        with open(CSV_FILE_USERS, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id=row['id']
                name=row['name']
                password=row['password']
                redis_client.hset(f"users:{id}", mapping={"id": id,"name": name, "password": password})
                redis_client.sadd("users",f"users:{id}")

if not redis_client.exists("quotes:1"):
    if os.path.exists(CSV_FILE_QUOTES):
        with open(CSV_FILE_QUOTES, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
               quote=row['quote']
               quote_id = redis_client.incr("quote_id")
               redis_client.hset(f"quotes:{quote_id}", mapping={"quote": quote})
               redis_client.sadd("quotes",f"quotes:{quote_id}")