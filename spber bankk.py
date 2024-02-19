#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('month', type=str)
parser.add_argument('year', type=str)
args = parser.parse_args()

month = args.month
year = args.year
if month != ...:
    raise ValueError('month gavno')
outcome_data = pd.read_excel(f"outcome_{month}.2024.xlsx")
outcome_data



outcome_data["День"] = [int(x.split()[0]) for x in outcome_data["Дата"]]
outcome_data



fig, ax = plt.subplots(constrained_layout=True)
sns.lineplot(
    data=outcome_data,
    x="День",
    y="Сумма",
    hue="Категория",
    ax=ax
)
ax.legend()
plt.show()



fig, ax = plt.subplots(constrained_layout=True)
plt.title(f'{month}.{year}')
sns.barplot(

    data=outcome_data,
    x="Сумма",
    y="Категория",
    orient = "h",
    estimator="sum",
    errorbar=None,
    ax=ax
)
plt.show()


# In[ ]:




