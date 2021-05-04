import sqlite3

conn = sqlite3.connect('bkfood.sqlite')
cur = conn.cursor()

print('Turning "NA" values to 0')

upd_na = "UPDATE Food SET serving_size = 0 WHERE serving_size = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET calories = 0 WHERE calories = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET fat_cal = 0 WHERE fat_cal = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET protein = 0 WHERE protein = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET fat = 0 WHERE fat = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET sat_fat = 0 WHERE sat_fat = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET trans_fat = 0 WHERE trans_fat = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET chol = 0 WHERE chol = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET sodium = 0 WHERE sodium = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET carbs = 0 WHERE carbs = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET fiber = 0 WHERE fiber = 'NA' "
cur.execute(upd_na)
conn.commit()

upd_na = "UPDATE Food SET sugar = 0 WHERE sugar = 'NA' "
cur.execute(upd_na)
conn.commit()

print('Database successfully modified')
print ('Top 10 BK caloric foods')
sqlstr = 'SELECT item, calories FROM Food ORDER BY calories DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
