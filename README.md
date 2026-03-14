# Notice
In our code, we used these Python libraries: `kagglehub`, `sqlite3`, `mathplotlib`, `seaborn`, `pandas`

# Files
```text
STA220_Movies/
├── tools/                 # A custome Python package
|   ├── __init__.py        # Package initialization for clean imports
|   └── sql_handling.py.py # Simplifies callings for sql queries by taking our database as default.
├── create_db.py           # Download the dataset on Kaggle, then convert the downloaded .csv file into sqlite database
└── revenue_budget.py      # Plot revenue v.s. budget; Count number of movies having extreme ratio between revenue and budget
```
