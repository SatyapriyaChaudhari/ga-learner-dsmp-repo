# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data = pd.read_csv(path)

#plt.hist(data['Rating'])
fig1=plt.figure()
data.hist(column="Rating")
plt.xlabel("Ratings")
plt.ylabel("Number of Apps")
plt.title("Rating Distribution")
plt.show()

data = data[data['Rating'] <= 5]
fig2=plt.figure()
data.hist(column="Rating")
plt.xlabel("Ratings")
plt.ylabel("Number of Apps")
plt.title("Rating Distribution")
plt.show()
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = total_null / data.isnull().count()
missing_data = pd.concat([total_null, percent_null], axis = 1, keys = ['Total','Percent'])
print("Missing Data:\n", missing_data)
print("=====================================================================")

data.dropna(how = 'any', inplace = True)
total_null_1 = data.isnull().sum()
percent_null_1 = total_null_1 / data.isnull().count()
missing_data_1 = pd.concat([total_null_1, percent_null_1], axis = 1, keys = ['Total','Percent'])
print("Missing Data:\n", missing_data_1)
# code ends here


# --------------

#Code starts here
fig = sns.catplot(x = "Category", y = "Rating", data = data, kind = "box", height = 10)
fig.set_xticklabels(rotation=90)
plt.title("Rating vs Category [BoxPlot]")

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].count)
data['Installs'] = data['Installs'].map(lambda x: (x.replace(',','').replace('+','')))
data['Installs'] = pd.to_numeric(data['Installs'], downcast = 'integer')
print(data['Installs'].head())
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
fig = sns.regplot(x = "Installs", y = "Rating", data = data)
plt.title("Rating vs Installs [RegPlot]")

#Code ends here


# --------------
#Code starts here
print(data['Price'].count)
#data['Installs'] = data['Installs'].map(lambda x: (x.replace(',','').replace('+','')))
data['Price'] = data['Price'].map(lambda x : (x.replace('$','')))
#data['Installs'] = pd.to_numeric(data['Installs'], downcast = 'integer')
data['Price'] = pd.to_numeric(data['Price'], downcast = 'float')
print(data['Price'].head())
fig = sns.regplot(x = "Price", y = "Rating", data = data)
plt.title("Rating vs Price [RegPlot]")

#Code ends here


# --------------
#Code starts here

print(data['Genres'].unique())
data['Genres'] = data['Genres'].map(lambda x : (x.split(';')[0]))
print(data['Genres'].head())
gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()
#gr_mean = data[['Genres', 'Rating']].groupby(['Genres']).mean()
print(gr_mean.describe())
#print(gr_mean.head)
gr_mean = gr_mean.sort_values(['Rating'])
print("First Value: ", gr_mean.iloc[0])
print("Last Value: ", gr_mean.iloc[-1])

#Code ends here


# --------------
#Code starts here
print(data['Last Updated'].head())
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()
print(max_date)
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
fig = sns.regplot(x = "Last Updated Days", y = "Rating", data = data)
plt.title("Rating vs Last Updated [RegPlot]")

#Code ends here


