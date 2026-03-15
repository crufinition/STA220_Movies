import sqlite3 as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
db = sql.connect('movies_data.db')


query = """
SELECT m.movie_id, m.budget, m.revenue, m.vote_average, m.vote_count, c.company
FROM movies m
JOIN movie_companies mc ON m.movie_id = mc.movie_id
JOIN companies c ON mc.company_id = c.company_id
"""

df_all = pd.read_sql(query, db)
print(df_all.head)
db.close()
import numpy as np
import pandas as pd
df_final = df_all[(df_all['budget'] >= 100000)&(df_all['revenue'] >= 10000)&(df_all['vote_count']>=10)].copy()
df_final['log_budget'] = np.log10(df_final['budget'])
df_final['log_revenue'] = np.log10(df_final['revenue'])
df_final= df_final.sort_values('budget', ascending=False)

print(f"Total movies I want: {len(df_final)}")
print(df_final.head())
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

#sns.regplot(data=df_final, x='log_budget', y='vote_average')
            #scatter_kws={'alpha':0.3, 'color':'steelblue'},
            #line_kws={'color':'red'}
            #)
sns.scatterplot(data=df_final, x='log_budget', y='vote_average')

plt.title('Higher Budget Buy a Better Rating?', fontsize=14, fontweight='bold')
plt.xlabel('Budget (USD)', fontsize=12)
plt.ylabel('Vote Average (Rating)', fontsize=12)
plt.show()
