import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

con = sqlite3.connect("bkfood.sqlite")
bk_meal = pd.read_sql_query("SELECT item, calories FROM Food ORDER BY calories DESC LIMIT 10", con)
print(bk_meal.head())

table = pd.pivot_table(data=bk_meal,index='item',values='calories',aggfunc=np.sum)
table

#bar graph
plt.bar(table.index,table['calories'])

#xticks
plt.xticks(rotation=70)

#x-axis labels
plt.xlabel('Food item')

#y-axis labels
plt.ylabel('Caloric amount')

#plot title
plt.title('Top 10 caloric food items in BK Menu')

#save plot
plt.savefig('graph.png',dpi=300,bbox_inches='tight')

print('Graph successfully saved')
