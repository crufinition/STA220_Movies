from tools.sql_handling import *
import matplotlib.pyplot as plt
import seaborn as sns

vote_df = my_sql("""
                SELECT
                  movie_id,
                  budget,
                  revenue,
                  vote_average,
                  vote_count,
                  LOG(budget) AS log_budget,
                  LOG(revenue) AS log_revenue
                FROM movies
                WHERE budget >= 1e+4
                AND revenue >= 1e+4
                AND vote_count >= 10
                ORDER BY budget DESC
""")

print(f"Total movies I want: {len(vote_df)}")
print(vote_df.head())

plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

#sns.regplot(data=vote_df, x='log_budget', y='vote_average')
            #scatter_kws={'alpha':0.3, 'color':'steelblue'},
            #line_kws={'color':'red'}
            #)
sns.scatterplot(data=vote_df, x='log_budget', y='vote_average')

plt.title('Higher Budget Buy a Better Rating?', fontsize=14, fontweight='bold')
plt.xlabel('Budget (USD)', fontsize=12)
plt.ylabel('Vote Average (Rating)', fontsize=12)
plt.show()
