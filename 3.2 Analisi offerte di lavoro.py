import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset

dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

print("--- Prime 5 righe del DataFrame ---")
print(df.head())

grouped_country = df.groupby('country')['salary_year_avg'].agg(    salary_mean='mean',
    job_count='count',
    salary_min='min',
    salary_max='max'
    ).reset_index()

print("\n--- Statistiche salariali per Paese ---")
print(grouped_country)

job_salary = df.groupby('job_title_short')['salary_year_avg'].mean().sort_values(ascending = False)

print("\n--- Salario medio per Ruolo (ordinato) ---")
print(job_salary)

plt.figure(figsize=(10,8))
plt.barh(job_salary.index, job_salary.values, color='skyblue')
plt.title('Stipendio Medio Annuale per Tipo di Lavoro')
plt.xlabel('Stipendio Medio')
plt.ylabel('Tipo di Lavoro')
plt.tight_layout()
plt.show()
