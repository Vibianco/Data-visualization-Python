import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('bkfood.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Food (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    item TEXT,
    serving_size INTEGER,
    calories FLOAT,
    fat_cal FLOAT,
    protein FLOAT,
    fat FLOAT,
    sat_fat FLOAT,
    trans_fat FLOAT,
    chol FLOAT,
    sodium FLOAT,
    carbs FLOAT,
    fiber FLOAT,
    sugar FLOAT,
    meat INTEGER);''')

fh = open("burger-king-items.txt")
print('Loading BK Items into database')
for line in fh:
    if line.startswith('Item'): continue
    words = line.split()
    item = words[0]
    serving_size = words[1]
    calories = words[2]
    fat_cal = words[3]
    protein = words[4]
    fat = words[5]
    sat_fat = words[6]
    trans_fat = words[7]
    chol = words[8]
    sodium = words[9]
    carbs = words[10]
    fiber = words[11]
    sugar = words[12]
    meat = words[13]
    if serving_size is None or calories is None or fat_cal is None or protein is None or fat is None or sat_fat is None or trans_fat is None or chol is None or sodium is None or carbs is None or fiber is None or sugar is None or meat is None : continue
    cur.execute('''INSERT OR IGNORE INTO Food (item, serving_size, calories, fat_cal, protein, fat, sat_fat, trans_fat, chol, sodium, carbs, fiber, sugar, meat)
    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', (item, serving_size, calories, fat_cal, protein, fat, sat_fat, trans_fat, chol, sodium, carbs, fiber, sugar, meat ))

print('Items loaded successfully into database')

conn.commit()
cur.close()
