import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("olympics_08_medalists")
print("Original ('Untidy') DataFrame:") 
print(df)

## Firstly Lets untity the data! Looking at Atheletes, countries, their sport, and their medals.  
df_melted = pd.melt(df, 
                    id_vars= ['medalist_name'], 
                    var_name='event_gender', 
                    value_name='medal'
                    )
display(df_melted.head(10))

# Firstly, looking at those who didn't palce, and correting N/A for their medal placement
df_melted['medal'] = df_melted['medal'].fillna('N/A')

#Next Split 'event_gender' so they are two columns
df_melted[['gender','event']] = df_melted['event_gender'].str.split('_', expand=True)

# Let's tidy up the metal 'type' column 
df_melted['Medal_Type'] = df_melted['Medal_Type'].str.replace('Medal_', ' ')

# Split the names of Atheltes!
df[['First_Name', 'Last_Name']] = df['medalist_name'].str.split(' ', expand=True)

#Drop the data/columns unwanted (specifcally just event and gender and medalist names)
df_melted.drop(columns=['event_gender'])
df.drop(columns=['medalist_name'], inplace=True)

#Final Clean Data! 
print("New (Tidy/Melted) DataFrame:")
df_melted

# Find Visulations Below

#Histplot
sns.histplot(data=df_melted, x="gender", hue="Country")
plt.title("Olympics 2008 Distribution of Medal Counts by Country")
plt.xlabel("Number of Medals")
plt.ylabel("Frequency")
plt.show()

#Barplot
sns.barplot(data=df_melted, x = "Country", hue = "medal", multiple = "Stack")
plt.title("Olympics 2008 Distribution of Medals Country")
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.show()


#Pivot Table

pivot_table_medalists = pd.pivot_table(df_melted, values='medal', 
                                       index='event', columns='gender', 
                                       aggfunc='count'
                                       )

print("\nPivot Table (Medal Count by Gender):")
print(pivot_table_medalists)