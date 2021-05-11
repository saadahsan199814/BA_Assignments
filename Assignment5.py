#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


data_dict = {'name': ['Nancy','Andrew','Janet','Margaret', 'Steven'], 'monthly_salary':[5000, 4000, 6000, 3000, 2000], 
             'zip':[98122, 98401, 98033, 98052, 98051]}
print('First, print the dict:')
print(data_dict)   


# In[9]:


emp_df = pd.DataFrame(data_dict)


# In[10]:


print(emp_df)                     
print('\n', type(emp_df))


# In[11]:


print(emp_df.shape)


# In[12]:


print(emp_df['name'])


# In[13]:


print(emp_df['zip'])


# In[14]:


print(emp_df.columns)


# In[16]:


print(emp_df.columns)


# In[17]:


first_row = emp_df.iloc[0]


# In[18]:


print(first_row)


# In[21]:


last_row = emp_df.iloc[4]


# In[22]:


print(last_row)


# In[23]:


print('The shape is:', emp_df.shape)  


# In[24]:


print('The size is:', emp_df.size)


# In[30]:


print(emp_df[['monthly_salary']].mean(axis=0))


# In[31]:


first_column = emp_df.iloc[:,0]


# In[32]:


sort_column = sort_index(first_column)


# In[35]:


emp_df.sort_values(by = ['name'], inplace= True)


# In[36]:


print(emp_df)


# In[39]:


emp1_df = emp_df[emp_df['zip'] == 98033]


# In[40]:


print(emp1_df)


# In[44]:


emp_df['annual_salary'] = emp_df['monthly_salary']*12


# In[45]:


print(emp_df['annual_salary'])


# In[50]:


emp_df = emp_df.rename(columns={'name':'firstname'})


# In[49]:


print(emp_df['firstname'])


# In[55]:


emp_info = emp_df[['firstname', 'annual_salary', 'zip']].copy()


# In[56]:


print(emp_info)


# In[57]:


print(emp_info['firstname'])


# In[58]:


emp_info = emp_info.drop('annual_salary', axis = 1) 


# In[59]:


print(emp_info)


# In[ ]:




