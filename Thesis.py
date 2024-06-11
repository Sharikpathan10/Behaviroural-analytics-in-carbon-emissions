import pandas as pd
from zipfile import ZipFile
import seaborn as sns
import matplotlib.pyplot as plt

# Unzipping the file
dataset_path = 'train.csv.zip'
with ZipFile(dataset_path, 'r') as zip_ref:
    zip_ref.extractall()

# Loading the dataset
df = pd.read_csv('train.csv')

# Displaying the first few rows to understand the key variables
print(df.head())

# Plotting the count of buildings by year built (after 1920)
plt.figure(figsize=(24, 6))
sns.countplot(x='year_built', data=df[df.year_built > 1920])
plt.xticks(rotation=90)
plt.title('Count of Buildings by Year Built (After 1920)')
plt.show()

# Plotting the boxplot of site EUI by year built
plt.figure(figsize=(20, 6))
sns.boxplot(x="year_built", y="site_eui", data=df)
plt.xticks(rotation=90)
plt.title('Site EUI by Year Built')
plt.show()

# Convert Year_Factor to a more meaningful year representation if needed
# Assuming Year_Factor is already in a usable format for trend analysis
# Grouping by Year_Factor and calculating average site_eui
yearly_energy_consumption = df.groupby('Year_Factor')['site_eui'].mean().reset_index()

# Plotting trends in energy consumption over the years
plt.figure(figsize=(10, 6), facecolor='white')
plt.plot(yearly_energy_consumption['Year_Factor'], yearly_energy_consumption['site_eui'], marker="o")
plt.title('Trends in Energy Consumption Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Site EUI')
plt.grid(True)
plt.show()

# Correlation Between Floor area and building class
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='floor_area', hue='building_class', y='site_eui')
plt.title('Correlation Between Floor Area and Building Class')
plt.show()

# Distribution of Floor_area with respect to energy_star_rating on the basis of States
plt.figure(figsize=(20, 6))
sns.scatterplot(data=df, y='floor_area', hue='State_Factor', x='energy_star_rating')
plt.title('Distribution of Floor Area with respect to Energy Star Rating by State')
plt.show()

# How does energy consumption correlate with weather variables such as temperature and precipitation?
weather_variables = ['avg_temp', 'precipitation_inches', 'snowfall_inches', 'cooling_degree_days', 'heating_degree_days', 'site_eui']
correlation_matrix = df[weather_variables].corr()

# Plotting the correlation matrix
plt.figure(figsize=(10, 8), facecolor='white')
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Energy Consumption and Weather Variables')
plt.show()

# Grouping by facility_type and calculating average site_eui for each type
building_energy_consumption = df.groupby('facility_type')['site_eui'].mean().sort_values(ascending=False).reset_index()

# Selecting the top 10 most energy-consuming building types
top_building_types = building_energy_consumption.head(10)

# Plotting
plt.figure(figsize=(12, 6), facecolor='white')
plt.barh(top_building_types['facility_type'], top_building_types['site_eui'], color='skyblue')
plt.title('Top 10 Building Types by Average Energy Consumption')
plt.xlabel('Average Site EUI')
plt.ylabel('Building Type')
plt.gca().invert_yaxis()  # to display the highest consuming building at the top
plt.show()

