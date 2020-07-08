#!/usr/bin/env python
# coding: utf-8

# In[1]:


import win32com.client as win32ComClient
import pandas as pd
 
# create empty pandas DataFrame
idea_df = pd.DataFrame()
 
if __name__ == "__main__":
       try:
             idea = win32ComClient.Dispatch(dispatch="Idea.IdeaClient")
             db = idea.CurrentDatabase()
            
             # Object to read table definitions
             tdef = db.TableDef()
            
             # Objects to read data
             rs = db.RecordSet()
             rec = rs.ActiveRecord()
            
             for col in range(1, rec.NumberOfFields + 1):
                    data_list = []
                    for row in range(1, rs.Count + 1):
                           rs.GetAt(row)
                           data_list.append(rec.ValueAt(col))
 
                    # append each column after reading to DataFrame
                    idea_df[tdef.GetFieldAt(col).Name] = data_list
            
       finally:
             db = None
             idea = None
             tdef = None
             rs = None
             rec = None


# In[ ]:




