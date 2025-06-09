import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import Normalizer, OneHotEncoder


#Read the dataset into a Pandas DataFrame
df = pd.read_csv('flavors_of_cacao.csv')
df_temp = df.copy()


#delete the missing value entries
df = df.dropna()


#How many tuples are there in the dataset?
# Assume the length of data set is requested!
tuple_count = len(df)


#How many unique company names are there in the dataset?
company_name_len = len(df['Company\xa0\n(Maker-if known)'].unique())


#How many reviews are made in 2013 in the dataset?
rev_num_2013 = len(df[df['Review\nDate']==2013])


#In the BeanType Column, how many missing values are there?
Missed_BinType = df_temp['Bean\nType'].isna().sum()


#Visualize the rating column with a histogram
rating_hist = sns.histplot(df['Rating'], stat='percent', label='Data Histogram', common_norm=True)
rating_hist.set_ylabel('Percentage (%)')
plt.show()

#Comment on the resulting figure!
cmnt = f'''Based on the histogram, most of the ratings are around 3.5/5.
Also, the distribution of the ratings is close to normal
            '''
print(cmnt)


#Plot the converted numerical Cocoa Percent values against the Rating values!
df['Cocoa\nPercent'] = df['Cocoa\nPercent'].str.replace('%','').astype(float)/100
scat_plt = plt.scatter(x=df['Cocoa\nPercent'], y=df['Rating'], alpha=0.1)
scat_plt.axes.set_xlabel('Percentage (%)')
scat_plt.axes.set_ylabel('Rating (%)')
plt.show()
print('More cocoa in a bar does not correspond to a higher rating!')


#Normalize the Rating Column and print the results.
norm = Normalizer()
df['Rating'] = norm.fit_transform(df[['Rating']])


#List the companies ordered by their average score (averaged over each company’s reviews).
names = df['Company\xa0\n(Maker-if known)'].unique()
mean_lst = []
for i in names:
    print(i)
    mean_lst.append(float(df_temp.iloc[df[df['Company\xa0\n(Maker-if known)']==i].index,6].mean()))
mean_list_df = pd.DataFrame(mean_lst)
names = pd.DataFrame(names)
company_by_rev = pd.concat([names,mean_list_df],axis=1)
company_by_rev.columns = ['Names','Avg_Rev_Score']
company_by_rev.sort_values(by='Avg_Rev_Score',ascending=False)
print(company_by_rev)


#Suppose we are interested in the company’s names and locations for some collective analysis. Encode the two categorical columns with the encoder you think is best for the job!
encoder = OneHotEncoder()
df_encoded = encoder.fit_transform(df.select_dtypes('object'))