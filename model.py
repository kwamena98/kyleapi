import psycopg2
import os


conn = psycopg2.connect(
    dbname="derrickdb",
    user="derrickson",
    password="ww2DadsonKwamena",
    host="172.105.148.175",
    port="5432"
)

cur = conn.cursor()



command ="""
    CREATE TABLE ambittmedia_clients(
    id SERIAL,
    email VARCHAR(10000),
    name VARCHAR(20000),
    session_id VARCHAR(100000),
    phone_number VARCHAR(40000)
    )

"""

cur.execute(command)
conn.commit()