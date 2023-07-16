import numpy as np
import pandas as pd

technologies = ['Java', 'python', 'C#', 'C++', 'R']
fee = [10000, 30000, 20000, 10000, 30000]
duration = ['50 Days', '60 Days', np.nan, '30 Days', '30 Days']
discount = [2000, 1000, 800, 500, 1000]
columns = ['Course', 'Duration', 'Fee', 'Discount']

df = pd.DataFrame(list(zip(technologies, duration, fee, discount)), columns=columns)
df.to_excel('course_details.xlsx')

path = 'course_details.xlsx'

dataset = pd.read_excel(path)
print(dataset)

print('\n******Operation on DataFrame******')
print('1.Fetching First Row in DataSet')
frow = df.head(1)
print(frow)

print('\n2.Fetching Column in DataSet')
col = df.Course
col2 = df.Fee
print(col)
print(col2)

print('\n3.Aggregate functions')

mean_fee = df['Fee'].mean()
max_fee = df['Fee'].max()
min_fee = df['Fee'].min()
sum_fee = df['Fee'].sum()
count_discount = df['Discount'].count()

print(f'Mean Fee:{mean_fee}')
print(f'Max Fee:{max_fee}')
print(f'Minimum Fee:{min_fee}')
print(f'Discount Count:{count_discount}')
print(f'Total Fee:{sum_fee}')

print('\n4.Adding new Column')
dataset['Total cost'] = dataset['Fee'] - dataset['Discount']
print(dataset)
