import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset

dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

grouped_country = df.groupby('country')['salary_year_avg'].agg(    salary_mean='mean',
    job_count='count',
    salary_min='min',
    salary_max='max'
    ).reset.index()

job_salary = df.groupby('job_title_short')['salary_year_avg'].mean().sort_values(ascending = True)

plt.figure(figsize=(10,8))
plt.title('Stipendio Medio Annuale per Tipo di Lavoro')
plt.xlabel('Stipendio Medio')
plt.ylabel('Tipo di Lavoro')
plt.tight_layout()
plt.show()