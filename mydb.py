import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

database = mysql.connector.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
)
cursorObject = database.cursor()
db_name = os.getenv('DB_NAME')

cursorObject.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')

print('Database created successfully')