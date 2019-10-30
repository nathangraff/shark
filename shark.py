#!/usr/bin/env python
# coding: utf-8

# In[3]:


ss = '2019'


# In[5]:


ss.isnumeric()


# In[6]:


import pyodbc


# In[55]:


conn = pyodbc.connect('DSN=kubricksql;UID=DE14;PWD=password')


# In[56]:


cur = conn.cursor()


# q = 'select * from nathan.shark'

# data = cur.execute(q)
# for row in data:
#     print(row) 

# In[59]:


q = 'insert into nathan.shark([attack_date], [case_number], [country], [activity], [age], [gender], [isfatal]) values (?, ?, ?, ?, ?, ?, ?)'
p = ['2019-04-03', '15ac5', 'USA', 'fish tank', 6, 'f', 0]


# In[60]:


try:
    data = cur.execute(q,p)
    conn.commit()
except: 
    conn.rollback()


# In[62]:


import csv 
from datetime import datetime,timedelta


# In[ ]:


import pyodbc
conn = pyodbc.connect('DSN=kubricksql;UID=DE14;PWD=password')
cur = conn.cursor()


# In[64]:


sharkfile = r'c:\data\GSAF5 (1).csv'


# In[65]:


attack_dates = []
isfatal = []
case_number = []
country = []
activity = []
age = []
gender = []
with open(sharkfile) as f:
    reader = csv.DictReader(f)
    for row in reader:
        attack_dates.append(row['Date'])
        isfatal.append(row['Fatal (Y/N)'])
        case_number.append(row['Case Number'])
        country.append(row['Country'])
        activity.append(row['Activity'])
        age.append(row['Age'])
        gender.append(row['Sex '])


# In[88]:


data = zip(attack_dates, case_number, country, activity, age, gender, isfatal)


# In[ ]:


cur.execute('truncate table nathan.shark')


# In[89]:


q = 'insert into nathan.shark([attack_date], [case_number], [country], [activity], [age], [gender], [isfatal]) values (?, ?, ?, ?, ?, ?, ?)'
p = ['2019-04-03', '15ac5', 'USA', 'fish tank', 6, 'f', 0]


# In[90]:


for d in data:
    try:
        data = cur.execute(q,d)
        conn.commit()
    except: 
        conn.rollback()


# In[80]:





# In[ ]:




