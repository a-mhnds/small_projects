import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import Normalizer, OneHotEncoder


#Read the dataset into a Pandas DataFrame
df = pd.read_csv('results.csv')
df_temp = df.copy()


#check missing values
if (df.isna().sum()==0).all():
    print('No missing value in the dataset.')
else:
    df = df.dropna()
    print('Missing values found and removed.')


#How many tuples are there in the dataset?
# Assume the length of data set is requested!
tuple_count = len(df)


#How many tournaments are there in the dataset?
print('Number of tournaments is: ', len(df['tournament'].unique()))


#Convert the column date to timestamps!
df['date'] = pd.to_datetime(df['date'])


#Find out how many matches in the dataset were played in 2018.
print('Number of matches in 2018: ', (df['date'].dt.year==2018).sum())


#Calculate how many times the home team won, lost, or had a draw.
home_results = []
for i in range(len(df)):
    if df.iloc[i,3] > df.iloc[i,4]:
        home_results.append(1)
    elif df.iloc[i,3] < df.iloc[i,4]:
        home_results.append(2)
    else:
        home_results.append(0)
home_results = pd.DataFrame(home_results)
print(f'''Home team won for {home_results.value_counts()[1]} times
      Home team lost for {home_results.value_counts()[2]} times.
      Home team had a draw for {home_results.value_counts()[0]}''')


#Visulaization
home_results_count = [home_results.value_counts()[1], home_results.value_counts()[2], home_results.value_counts()[0]]
keys = ['Won', 'Lost', 'Draw']
palette_color = sns.color_palette('bright')
plt.pie(home_results_count, labels=keys, colors=palette_color, autopct='%.0f%%')


#Plot the neutral column as a pie chart.