# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 08:05:59 2022

@author: c computer
"""
#Firstly, we import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#we import it to a variable with pandas library function .read_csv()
data = pd.read_csv('global-hunger-index.csv')
#what does the data look do you know? , well I know cause I used the pandas head() function that returns the first few entities of the data frame.
print(data.head())
#attributes like data types, is it not null the number of rows and columns present we do that with .info() function in pandas
print(data.info())
#using .describe() such as count, mean, standard deviation, minimum, maximum and quartiles 1,2 and 3.
print(data.describe())
#Let’s see the count of each column present in the data frame
print(data.count())
#see the count of each particular country with respect to the global hunger index for the years mentioned
print(data.Entity.value_counts())

#Since the dataset is big we need to change the figure size of the graph so that it can be displayed correctly
sns.set(rc={'figure.figsize':(70,40)})
#Based on the data seen we use the histogram for graphical representation
sns.histplot(y = data.Entity.unique(), x = data.Entity.value_counts())
#To identify the outliers and the range of the same we use the box plot
sns.boxplot(x= data.Year, y = data['Global Hunger Index (2021)'] , palette=["m", "g"])

#We get the unique values of countries and years both as they are repeated quite often using the .unique() function in pandas.
country_name = data.Entity.unique()
years = data.Year.unique()
#We use the .corr() function in pandas to get correlation of the data attributes with each other.
print(data.corr())

'''A negative correlation meaning with a year increase GHI is decreasing though this is a 
very vague statement as the whole countries, in general, are going down, but not the 
individual countries.A negative correlation meaning with a year increase GHI is decreasing 
though this is a very vague statement as the whole countries, in general, are going down, 
but not the individual countries.'''