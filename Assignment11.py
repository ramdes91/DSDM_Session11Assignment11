
# coding: utf-8

# In[80]:


#Initialize#

import pandas as pd 
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays':  [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})

df


# In[81]:


#1.Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column (instead of a float column).#

df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
df


# In[82]:


#2. The From_To column would be better as two separate columns! Split each string on the underscore delimiter _ to give a new temporary DataFrame with the correct values.Assign the correct column names to this temporary DataFrame.#

tmpDF = pd.DataFrame(columns=['From','To'])
tmpDF[['From','To']] = df['From_To'].str.split('_', expand=True)
tmpDF


# In[83]:


#3. Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)#

tmpDF['From'] = tmpDF.From.str.title()
tmpDF['To'] = tmpDF.To.str.title()
tmpDF


# In[84]:


#4. Delete the From_To column from df and attach the temporary DataFrame from the previous questions.#

df=pd.concat([tmpDF,df], axis=1)
df = df.drop('From_To', 1)
df


# In[85]:


#5. In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN. Expand the Series of lists into a DataFrame named delays, rename the columns delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df with delays.#

tDelay = pd.DataFrame(df.RecentDelays)
tDelay = pd.DataFrame(df['RecentDelays'].values.tolist())
tDelay.columns = ['Delay_1', 'Delay_2', 'Delay_3']
df = df.drop('RecentDelays', 1)
df.insert(3, "Delay_1", tDelay['Delay_1'])
df.insert(4, "Delay_2", tDelay['Delay_2'])
df.insert(5, "Delay_3", tDelay['Delay_3'])
df

