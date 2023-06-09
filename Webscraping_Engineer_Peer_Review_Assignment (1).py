#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork899-2023-01-01">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # Peer Review Assignment - Data Engineer - Webscraping
# 

# Estimated time needed: **20** minutes
# 

# ## Objectives
# 
# In this part you will:
# 
# - Use webscraping to get bank information
# 

# For this lab, we are going to be using Python and several Python libraries. Some of these libraries might be installed in your lab environment or in SN Labs. Others may need to be installed by you. The cells below will install these libraries when executed.
# 

# In[4]:


#!mamba install pandas==1.3.3 -y
#!mamba install requests==2.26.0 -y
get_ipython().system('mamba install bs4==4.10.0 -y')
get_ipython().system('mamba install html5lib==1.1 -y')


# ## Imports
# 
# Import any additional libraries you may need here.
# 

# In[19]:


from bs4 import BeautifulSoup
#import html5lib
import requests
import pandas as pd


# ## Extract Data Using Web Scraping
# 

# The wikipedia webpage https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks provides information about largest banks in the world by various parameters. Scrape the data from the table 'By market capitalization' and store it in a JSON file.
# 

# ### Webpage Contents
# 
# Gather the contents of the webpage in text format using the `requests` library and assign it to the variable <code>html_data</code>
# 

# In[13]:


#Write your code here
html_data = requests.get("https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks").text
print(html_data)


# <b>Question 1</b> Print out the output of the following line, and remember it as it will be a quiz question:
# 

# In[14]:


html_data[760:783]


# ### Scraping the Data
# 
# <b> Question 2</b> Using the contents and `beautiful soup` load the data from the `By market capitalization` table into a `pandas` dataframe. The dataframe should have the bank `Name` and `Market Cap (US$ Billion)` as column names.  Display the first five rows using head. 
# 

# Using BeautifulSoup parse the contents of the webpage.
# 

# In[21]:


#Replace the dots below
soup = BeautifulSoup(html_data, 'html.parser')
soup = soup.find('table', class_='wikitable sortable mw-collapsible')
print(soup)


# Load the data from the `By market capitalization` table into a pandas dataframe. The dataframe should have the bank `Name` and `Market Cap (US$ Billion)` as column names. Using the empty dataframe `data` and the given loop extract the necessary data from each row and append it to the empty dataframe.
# 

# In[34]:


data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

rows = []
for tr in soup.find_all('tr')[1:]:
    row = [td.text for td in tr.find_all('td')[1:]]
    rows.append(row)
data = pd.DataFrame(rows,columns=["Name","Market Cap (US$ Billion)"])


# **Question 3** Display the first five rows using the `head` function.
# 

# In[35]:


#Write your code here
print(data.head(5))


# 
# ### Loading the Data
# 
# Load the `pandas` dataframe created above into a JSON named `bank_market_cap.json` using the `to_json()` function.
# 

# In[37]:


#Write your code here
data.to_json("bank_market_cap.json")


# ## Authors
# 

# Ramesh Sannareddy, Joseph Santarcangelo and Azim Hirjani
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2022-07-12        | 0.2     | Appalabhaktula Hema | Corrected the code and markdown |
# | 2020-11-25        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

# Copyright © 2020 IBM Corporation.
# 
