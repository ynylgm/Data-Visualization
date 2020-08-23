import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://github.com/ynylgm/Data-Visualization/blob/master/import/1999-2017-import.csv?raw=true')
df.drop(columns=['U.S. food imports, estimated value by country'], inplace=True)
df.columns = df.iloc[0]
df.rename(columns={df.columns[0]:'Countries'},inplace=True)
df.columns = df.columns.fillna('to_drop')
df.drop('to_drop', axis = 1, inplace = True)
df = df.dropna()
df.reset_index(drop=True, inplace=True)
df.drop(df.index[11:65], inplace=True)
df.reset_index(drop=True, inplace=True)
df = df.T
df.iloc[0] = df.iloc[0].str.strip('(*)')
df.columns = df.iloc[0]
df = df.drop(['Countries']).rename_axis('Year').reset_index()
df = df.iloc[0:19, :]
for n in df.columns.tolist():
    df[n] = df[n].str.replace(',','').astype(float)
df['Year'] = df['Year'].astype(int)

plt.style.use('seaborn-whitegrid')
sns.set_style('whitegrid')
plt.figure(figsize=(16,9))
plt.plot('Year','Grand Total', data=df, marker='o')
plt.plot(2009.1, 82000, 'ro', markersize=115, fillstyle='none', markeredgewidth=2.8)
plt.xticks(np.arange(1999, 2018, 3), fontsize=13.3, y=-.01)
plt.yticks(fontsize=13)
sns.despine()
plt.yticks(ticks=np.arange(40000, 160000, 20000), labels=['40,000','60,000','80,000','100,000','120,000','140,000'])
plt.text(1997.95, 147600, 'Million $', fontsize=12)
plt.title(label='Total U.S. Food Imports from 1999 to 2017', loc='left', fontsize=17.5, y=1.05, x=-.013)
plt.margins(.045, .08)
plt.text(2007.8, 97500, 'Significant deficit\n       in 2009', fontsize=17, color='red')
plt.savefig('import-total.png')

plt.close()

plt.style.use('seaborn-whitegrid')
sns.set_style('whitegrid')
plt.figure(figsize=(16,9))
for col in df.columns[1:8]:
    plt.plot('Year',col, data=df)
plt.xticks(np.arange(1999, 2018, 2), fontsize=13, y=-.01)
plt.yticks(fontsize=13)
plt.axvspan(2008.4, 2009.6, color='grey', alpha=0.1)
sns.despine()
plt.title(label='U.S. Food Imports from Top 7 Countries from 1999 to 2017', loc='left', fontsize=17.5, y=1.048, x=-.008)
plt.legend(loc='upper left', bbox_to_anchor=(1.016, 1.0), fontsize=11.5)
plt.text(1997.95, 28100, 'Million $', fontsize=12)
plt.yticks(ticks=np.arange(0, 30000, 5000), labels=['0','5,000','10,000','15,000','20,000','25,000'])
plt.savefig('import-countries.png')
