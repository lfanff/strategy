
# coding: utf-8

## THIS IS THE FIRST STRATEGY BACKTEST

# In[4]:

import pandas as pd
AAPL_df = pd.read_csv('C:\\Users\\yz473\\fan\\AAPL.csv')


# In[5]:

import pandas as pd
GOOG_df = pd.read_csv('C:\\Users\\yz473\\fan\\GOOG.csv')


# In[7]:

import pandas as pd
AMZN_df = pd.read_csv('C:\\Users\\yz473\\fan\\AMZN.csv')


# In[38]:

#print AMZN_df

x = AMZN_df.Close
# tmp = pd.Series([0])
# print pd.concat(x[1:], tmp) 
x = x.drop(0)
x.index = range(0, len(x))

AMZN_df['prev_close'] = x

print AMZN_df





    



# In[ ]:



