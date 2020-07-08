#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import win32com.client as win32comclient

if __name__ == "__main__":
    idea = win32comclient.Dispatch(dispatch="Idea.IdeaClient")
    new_filename = idea.UniqueFilename("High Value")
    try:
        db = idea.opendatabase("BSEG.IMD")
        task = db.Extraction()
        task.IncludeAllFields
        task.AddExtraction(new_filename, "", "DMBTR_VZ > 5000")
        task.PerformTask(1, db.Count)
    finally:
	idea.RefreshFileExplorer()
	task = None
	db= None
	idea = None

