#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import the os module, for the os.walk function
import os
from pathlib import Path
from bs4 import BeautifulSoup
import codecs
 
# Set the directory you want to start from
rootDir = 'Data'
outputDir = 'ExtractedData'

Path(outputDir).mkdir(parents=True, exist_ok=True)

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        #extension = os.path.splitext(fname)[1]
        if fname.endswith('.html'):
            # Get full path
            fullPath = dirName + '/' + fname
            print('\t%s' % fullPath)
            # Open file for read
            f=codecs.open(fullPath, 'r', 'utf-8')
            # Set output path and create new file
            writeFileName = outputDir + '/' + fname.replace('html', 'txt')
            fw = open(writeFileName, 'w')
            # Read html file using BeautifulSoup library
            document= BeautifulSoup(f.read(), 'html.parser')
            # We are only interested in the <p> tags
            all_p = document.body.find_all('p')
            # Traverse through all the p tags, remove the tags and write the text in lower case to the output file
            for p in all_p:
                fw.write(p.get_text().lower())
            fw.close()


