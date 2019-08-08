from tabula import read_pdf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def extract_data():
    data_columns = ['Campus',
                    'Name',
                    'Job Title',
                    'FTE',
                    'Annual Base Pay']
    df_read = read_pdf('data/usnh_salary_book_2018.pdf',
                       pages='all',
                       pandas_options={'header': None})

    df_read.columns = data_columns

    print('Data dimension:', df_read.shape)
    df_read.to_csv('data/usnh_salary_book_2018_extracted.csv', index=False)
    return df_read


def salaries_individuals(roster):
    roster_joined = '|'.join(roster).lower()
    salaries = df.loc[df['Name'].str.lower().str.contains(roster_joined)].sort_values(by='Annual Base Pay',
                                                                                      ascending=False)
    print(salaries)
    return salaries


# df = extract_data()
df = pd.read_csv('data/usnh_salary_book_2018_extracted.csv')
df.info()
df['Annual Base Pay'] = df['Annual Base Pay'].apply(lambda x: x.lstrip('$').replace(',', ''))
df['Annual Base Pay'] = df['Annual Base Pay'].astype(float)

df.groupby(by='Job Title').count().sort_values(['Campus'], ascending=False)
plt.figure()
df.groupby(by='Job Title').count()['Campus'].plot(kind='pie')
plt.show()

max_salary = df['Annual Base Pay'].max()
max_salary_idx = df['Annual Base Pay'].idxmax()
print(df.iloc[max_salary_idx])

salaries_sorted = df.sort_values(by=['Annual Base Pay'], ascending=False)
highest_salaries = salaries_sorted.iloc[0:20]
lowest_salaries = salaries_sorted.iloc[-20:]
print('Highest salaries:')
print(highest_salaries)
print('Lowest salaries:')
print(lowest_salaries)

df['Annual Base Pay'].mean()
df['Annual Base Pay'].mode()
df['Annual Base Pay'].median()

prof_salaries = df.loc[df['Job Title'].str.lower().str.contains('professor')].sort_values(by='Annual Base Pay',
                                                                                          ascending=False)
prof_top10 = prof_salaries.iloc[0:10].reset_index()
prof_least10 = prof_salaries.iloc[-10:].reset_index()

# -------------------- Individuals
cs_names = ['Hatcher', 'Ruml',
            'Bartos', 'Petrik', 'Varki', 'Charpentier',
            'Dietz', 'Begum', 'Xu, Dongpeng' 'Weiner, James', 'Valcourt, Scott',
            'Narayan', 'Magnusson', 'Hausner', 'Graf, Ken', 'Gildersleeve',
            'Coleman, Betsy', 'Bochert', 'Plumlee', 'Lemon',
            'Kibler', 'Kitterman', 'Desmarais']
cs_salaries = salaries_individuals(cs_names)

oiss_names = ['Webber, Elizabeth', 'Chiarantona']
oiss_salaries = salaries_individuals(oiss_names)

temp_names = ['Lyon, Mark', 'Macmanes']
temp_salaries = salaries_individuals(temp_names)
