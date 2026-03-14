from tools.sql_handling import *
import matplotlib.pyplot as plt
import seaborn as sns

movie_rev_bud = my_sql('''
SELECT
  movie_id,
  revenue,
  budget,
  revenue*1.0/budget AS ratio,
  MAX(revenue*1.0/budget, budget*1.0/revenue) AS abs_ratio
FROM movies
WHERE revenue > 1e+4 AND budget > 1e+4
ORDER BY abs_ratio DESC
''')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='budget', y='revenue', data=movie_rev_bud)
plt.title('Revenue vs. Budget for Movies')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.xscale('log') # Use log scale
plt.yscale('log') # Use log scale
plt.grid(True, which='both', ls='--', c='0.7')
plt.show()

out_liers = movie_rev_bud[movie_rev_bud['abs_ratio'] > 1e+3]
print(f'Number of movies with absolute ratio larger than 1000: {out_liers.shape[0]}')