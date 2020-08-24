import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

df_raw = pd.read_csv('https://data.bts.gov/api/views/crem-w557/rows.csv?raw=true')
df = df_raw.loc[:, df_raw.columns.str.startswith('U.S. Airline Traffic')]
df.insert(0, column = 'Date', value = df_raw.Date)
df = df.dropna()
df = df.iloc[:,[0,4,5,6]]
df.Date = pd.to_datetime(df.Date)
df.Date = df.Date.dt.date
df.reset_index(drop=True, inplace=True)

def millions(x, pos):
    return '%1.fM' % (x * 1e-6)

formatter = FuncFormatter(millions)

plt.tight_layout()
plt.figure(figsize=(16,9))
sns.set_style('ticks')
plt.plot(df.iloc[:,0],df.iloc[:,1], lw=2.5, c='#808080')
plt.plot(df.iloc[:,0],df.iloc[:,3], lw=2.5, c='#9932CC')
plt.plot(df.iloc[:,0],df.iloc[:,2], lw=2.5, c='#DC143C')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('20'+'%y'))
plt.gca().yaxis.set_major_formatter(formatter)
sns.despine()
plt.text('2020-04-10', 5500000, 'April\n2020', fontsize=14.5)
plt.plot([df.at[38, 'Date'],df.at[39, 'Date']],
         [df.at[27, 'U.S. Airline Traffic - Total - Non Seasonally Adjusted'],
          df.at[27, 'U.S. Airline Traffic - Total - Non Seasonally Adjusted']],
         lw=4, alpha=.75, c='#808080')
plt.text('2020-04-12', 75000000, 'April\n2019', fontsize=14.5)
plt.text('2020-04-12', 72500000, '(Total)', fontsize=12.5)
plt.legend(['Total', 'Domestic', 'International'], loc='upper left', fontsize=13.5, frameon=False)
plt.title(label='U.S. Air Travel, 2017 to April 2020', loc='left', fontsize=22, y=1.048, x=-.008)
plt.savefig('air-travel.png')