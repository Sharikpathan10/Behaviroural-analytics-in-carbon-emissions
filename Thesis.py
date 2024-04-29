import pandas as pd 
from zipfile import ZipFile 
import seaborn as sns

#Unzipping the file
dataset_path = 'train.csv.zip'
with ZipFile(dataset_path,'r')as zip_ref:
    zip_ref.extractall()
#loading the dataset
df=pd.read_csv('train.csv')
#Displaying the first few rows to understand the key varaibles
df.head()

plt.figure(figuze=(24,6))
sns.countplot(x='year_built',data=train[(train.year_built>1920)])
plt.show()

plt.figure(figsize(20,6))
sns.boxplot(x="year_built",y="site_eui",data=df)
plt.xtricks(rotation=90)
plt.show()

#Convert Year_factor to a more meaningful year representation if needed
#Assuming Year_Factor is already in a usable format for trend analysis
#Groupin by year_Factor and calculating average site_eui
yearly_energy_consumption = df.groupby('Year_Factor')['site_eui'].mena().reset_index()

#plotting 
plt.figure(figsize=(10,6),facecolor='white')
plt.plot(yearly_energy_consumption['Year_Factor',yearly_energy_consumption['site_eui'],marker="o"])
plt.title('Treads in energy Consumption Over the Years')
plt.xlablel('Year')
plt.ylabel('Average Site EUI')
plt.grid(True)
plt.show()

#Correlation Between Floor area and building class
plt.figure(figure=(12,6))
sns.scatterplot(data=train,x='floor_area',hue='building_class',y='site_eui')
plt.show()

#15.Distribution of Floor_area wrt energy_star_rating on the basis of States
plt.figure(figsize=(20,6))
plt.subplot(1,2,1)
sns.scatterplot(data=train,y='floor_area',hue='State_Factor',x='energy_star_rating')

#16.	How does energy consumption correlate with weather variables such as temperature and precipitation?
Weather_variables=['avg_temp','precipitation_inches','snowfall_inches','coolong_degree_dayes','heating_degree_days','site_eui']
correelation_matrix =df[weather_variables].corr()
#plotting the correlation matix
plt.figure(figsize=(10,8),facecolor='white')
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',
            fmt='.2f')
plt.title('Correlation Matrix of Energy Consumption and Weather Variables')
plt.show()