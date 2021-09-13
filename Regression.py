#!/usr/bin/env python
# coding: utf-8

# In[6]:


from collections import defaultdict

import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


anscombes = pd.read_csv('Anscombes_Quartet.csv')


# In[8]:


anscombes.head()


# In[9]:


anscombes


# In[10]:


x1 = anscombes['x1']
x2 = anscombes['x2']
x3 = anscombes['x3']
x4 = anscombes['x4']

y1 = anscombes['y1']
y2 = anscombes['y2']
y3 = anscombes['y3']
y4 = anscombes['y4']


# In[14]:


f, axes = plt.subplots(2, 2, sharex=True, sharey=True)

f.suptitle("Anscombe's Quartet",fontsize=20)
# Make subplots farther from each other
f.subplots_adjust(hspace=0.5, wspace=0.2)

plt.xlim(3,20)
plt.ylim(2,14)

axes[0, 0].set_title('I', fontsize=20)
axes[0, 0].scatter(x1, y1, c="b", marker='o')
axes[0, 0].set(xlabel='x1', ylabel='y1')

axes[0, 1].set_title('II', fontsize=20)
axes[0, 1].scatter(x2, y2, c="b", marker='o')
axes[0, 1].set(xlabel='x2', ylabel='y2')

axes[1, 0].set_title('III', fontsize=20)
axes[1, 0].scatter(x3, y3, c="b", marker='o')
axes[1, 0].set(xlabel='x3', ylabel='y3')

axes[1, 1].set_title('IV', fontsize=20)
axes[1, 1].scatter(x4, y4, c="b", marker='o')
axes[1, 1].set(xlabel='x4', ylabel='y4')


# In[12]:


f, axes = plt.subplots(2, 2, sharex=True, sharey=True)

f.suptitle("Anscombe's Quartet",fontsize=20)

# Make subplots farther from each other
f.subplots_adjust(hspace=0.4, wspace=0.2)

plt.xlim(3,20)
plt.ylim(2,14)

axes[0, 0].set_title('I', fontsize=20)
axes[0, 0].set(xlabel='x1', ylabel='y1')
fit_1 = np.polyfit(x1, y1, 1)
fit_fn_1 = np.poly1d(fit_1) 
axes[0, 0].plot(x1, y1, 'bo', x1, fit_fn_1(x1), 'r-')

axes[0, 1].set_title('II', fontsize=20)
axes[0, 1].set(xlabel='x2', ylabel='y2')
fit_2 = np.polyfit(x2, y2, 1)
fit_fn_2 = np.poly1d(fit_2) 
axes[0, 1].plot(x2, y2, 'bo', x2, fit_fn_2(x2), 'r-')

axes[1, 0].set_title('III', fontsize=20)
axes[1, 0].set(xlabel='x3', ylabel='y3')
fit_3 = np.polyfit(x3, y3, 1)
fit_fn_3 = np.poly1d(fit_3) 
axes[1, 0].plot(x3, y3, 'bo', x3, fit_fn_3(x3), 'r-')

axes[1, 1].set_title('IV', fontsize=20)
axes[1, 1].set(xlabel='x4', ylabel='y4')
fit_4 = np.polyfit(x4, y4, 1)
fit_fn_4 = np.poly1d(fit_4) 
axes[1, 1].plot(x4, y4, 'bo', x4, fit_fn_4(x4), 'r-')


# In[ ]:




