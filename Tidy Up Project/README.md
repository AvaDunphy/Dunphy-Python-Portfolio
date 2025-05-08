# Tidy the 'Untidy' Data with Me! 🧹


## Tiding Up the Olympic Gold Medalists of 2008! 🏆
In this project, I looked into a data set involving the athletes in the 2008 Olympics. However, the original data was quite unkept. There were various columns with different information. It was a struggle to try and read what the data was trying to show the audience. Therefore, through a variety of techniques, I decided to approach the data and tidy it up. By using arguments such as ".melt()," ".str.replace()", ".drop," and ".str.split()", as well as including some graphs to display the data better, I was able to tidy up the formatting. This way, the readers (of the data) could gain a better holistic understanding of what the data was trying to portray. 


## My Goal 🏅
Reorganize the data provided, so that it is overall more pleasing to the audience.

## How I achieved my goal ✅
Though above I mentioned some of the specific techniques, and arguments that I employed to clean up the data, my main goal was to reorganize the data, clean up columns, take away unnecessary spaces, separate athletes, metals, and countries, and athlete's first and last names. Overall, in doing so, the formatting of the data looks significantly cleaner. Below look for the step-by-step way I approached the tidying process. 


# My Process?

## Step One 🥇 - Upload Data & Impliment "Tidying" Code

Firstly, I created the proper paths in my notebook so I could have access to the data and started my 'cleaning' process. Through a variety of tools used, a lot of which I found on the "Python Cheat Sheet," I was able to turn the data from long to wide. This allows for the datasheet to be much easier on the eye, and more comprehendible. In this step I employed the 'melt' argument, allowing me to provide better visualizations. Then, I split the column of gender and event, using the 'str.split' argument. After which, I used 'str.replace' allowing me to get rid of the '_' after the word medal. Then finally, I used the '.drop' function allowing me to get rid of the other columns of event_gender and medal. Overall, this was a great first step to creating better flow on the datasheet, but there was still more to do!


## Step Two 🥈 - Upload More Data

After, I decided to merge the second datasheet, allowing me to have more access to different data. More specifically, I was interested in looking at the medalist’s country data. Therefore, I made use of the .merge argument, allowing me to not only merge the data sheets but also allowing for me to select which specific columns I wanted to have in my final datasheet.


## Step Three 🥉 - Upload Visualizations (Hisograms)

To provide more context to the data set, I included two visualizations of the datasheet. Firstly, I used a histogram to depict the distribution of medal counts between females and males. This way I can get a good look at what kinds of medals males and females got, and how they compare to one another. However, I noticed that there were more medals awarded to women instead of men, so I decided to add a bar graph to look at the events and the genders. From this I learned that females compete in four more events than males do, thus providing evidence for the difference in the number of medals awarded to each gender.


## Step Four 🏅 - Upload More Visualizations (Pivot Plot)


Finally, I decided to create a pivot plot, allowing me to better understand males and females and their events. This way I can better understand how many athletes were awarded medals for their event, and how many were female or male. Though the table provided a lot of clarity, I also provided a heatmap, once again allowing me to compare how many men and women won medals in their event amongst different events.
