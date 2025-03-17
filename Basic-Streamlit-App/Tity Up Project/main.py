import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("olympics_08_medalists")
print("Original ('Untidy') DataFrame:") 
print(df)

## Firstly Lets untity the data! Looking at Atheletes, countries, their sport, and their medals.  
df_melted = pd.melt(df, 
                    id_vars= ['Athlete', 'Country', 'Sport'],
                    value_vars=['Gold', 'Silver', 'Bronze'],
                    var_name = 'Medal_type',
                    value_name = 'Count'
                    )
display(df_melted.head(10))

# Let's tidy up the metal 'type' column 
df_melted['Medal_Type'] = df_melted['Medal_Type'].str.replace('Medal_', ' ')

# Count --> Integer
df_melted['Count'] = df_melted['Count'].astype(int)

# Metal Counts --> Country 
df_melted.groupby(['Country', 'Medal_type']) ['Count'].sum().restet_index() 

#Final Clean Data! 
print("New (Tidy/Melted) DataFrame:")
df_melted

# Visulations 

#Histplot
plt.figure(figsize=(15,10))
sns.histplot(data=df_melted, x="Count", hue="Medal_Type", multiple="Stack")
plt.title("Olympics 2008 Distribution of Medal Counts by Type")
plt.xlabel("Number of Medals")
plt.ylabel("Frequency")
plt.show()

#Barplot
plt.figure(figsize=(15,10))
sns.barplot(data=df_melted, x = "Country", y = "Count", multiple = "Stack")
plt.title("Olympics 2008 Distribution of Country and Medal Count")
plt.show()



#Pivot Table
