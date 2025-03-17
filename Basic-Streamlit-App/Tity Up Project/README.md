import matplotlib.image as mpimg
### Tidy the 'Untidy' Data with Me! 🧹


## Tyding Up the Olympic Gold Medalists of 2008! 🏆
# In this project, I looked into a data set inlucding the athletes in the 2008 Olympics. However, the orginal data, was quite unkept. There were various collumns with different information. It was a struggle to try and read what the data was trying to show the audience. Therefore, through a variety of techniques, I decided to approach the data and tidy it up. Through using arguments such as ".melt()", ".str.strip()", ".astype", and ".str.split()", as well as including some graphs to better display the data, I was able to tidy up the formatting. This way, the readers (of the data), could gain a better wholeistic understanding of what the data was trying to protray. 

## My Goal 🏅
# Reorgnize the data provided, so that it is overall more pleasing to the audience.

## How I achieved my goal ✅
# Though above I mentioned some of the specific techniques, and arugments that I employed to clean up the data, my main goal was to reorganize the data, clean up columns, take away uncessary spaces, seprate atheletes, metals, and countries, and athlete's first and last names. Overall, in doing so, the formatting of the data looks signficantly cleaner. Below look for the step by step way I approached the tidying process. 

# My Process 🔍
# 1. ".melt()"
# Firstly, I applied .melt() to the data set to try and tidy up the different columns where the medal types are reshaped into a 'long format'. By applying the .melt(), I was able to group together the medal types (Gold/Silver/Bronze) into one column.

📸:

# 2. ".str.strip()"
# Secondly, to improve the visualzations of the data, I looked to get rid of spaces in the column names and values. I did so by using the '.str.strip()' code, allowing me to better tidy up the small erros. 

📸: 

# 3. ".astype" 
# Thirdly, the funcation ".astype" allows for me to turn the Count (if it is stored as a string) into an integer, thus allowing for the code to count the medals. 

📸: 

# 4. ".str.split" 
# By implimenting the ".str.split" function, I am able to split up the name data, so that atheltes first names and last names have different columns. This way, I can better organize the data, so that I can either just look at last or first names.

# Final Clean Data! 
# After taking the necessary precausions, you can see the final clean cut data!

## Analysis of the Visulations 📑

# Histogram Plot 📈
# This histogram takes a look at the medal counts by type of medal. Allowing for me to get a better look at the different countries affect the medal distribution.
📸: 

# Barplot 📊
#
📸:

## Pivot Table