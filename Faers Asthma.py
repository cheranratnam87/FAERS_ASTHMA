#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd

# Get current working directory
current_dir = os.getcwd()

# Navigate to data folder
data_dir = os.path.join(current_dir, "data")

# Read CSV file
df = pd.read_csv(os.path.join(data_dir, "faers_asthma.csv"), sep=",")


# In[2]:


print(df.head(20))


# In[3]:


selected_cols = df[['Suspect Product Names', 'Reason for Use', 'Suspect Product Active Ingredients', 'Reactions', 'Serious','Outcomes', 'Sex',
                   'Patient Age', 'Patient Weight','Reporter Type','Report Source', 'Concomitant Product Names','Country where Event occurred', 'Reported to Manufacturer?',]]
print(selected_cols)


# In[ ]:




