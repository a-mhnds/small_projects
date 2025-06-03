import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')


# Check nan values
if df.columns[df.isna().sum()].empty == False:
    print('There are missing data points.')
    df = df.transpose().dropna(axis=1).transpose()
    print('Rows with NAN values are removed.')
else:
    print('There is NO missing data points.')


#Dropping Unnecessary Columns
df_refined = df.drop('diagnosis', axis=1)   #This column is target.
df_refined = df_refined.drop('id', axis=1)   #This column is target.
col_names = df_refined.columns

#Scaling
scaler = StandardScaler()
df_refined = scaler.fit_transform(df_refined)


#Encoding
target = df['diagnosis'].apply(lambda x: 1 if x=='M' else 0) #The target column is label encoded separatedly.


#Normalization
from sklearn.preprocessing import Normalizer
norm = Normalizer()
df_refined = norm.fit_transform(df_refined)


#save to data_refined.csv
df_refined = pd.DataFrame(df_refined, columns=col_names)
df_refined.to_csv('df_refined.csv')


#------------------------------------------------------------------------Visulization


#Correlation Matrix heat map
corr = df_refined.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.color_palette("light:#5A9", as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5, 'label': 'Correlation coef'})
ax.set_title('Correlation Heat Map', fontsize = 20, fontweight='bold')
plt.show()



#Pair Plots for the features
pair = sns.pairplot(df_refined,
             x_vars=['radius_mean', 'smoothness_mean', 'fractal_dimension_mean'],
             y_vars=['radius_worst','perimeter_worst'],
             kind='scatter', plot_kws=dict(color= 'k'))

plt.subplots_adjust(top=0.9)

plt.suptitle('pairplots for Selected Features', fontsize=20)
plt.show()

