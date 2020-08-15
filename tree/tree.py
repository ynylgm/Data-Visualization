import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pywaffle import Waffle
import os

df_raw = pd.read_csv('https://raw.githubusercontent.com/ynylgm/Data-Visualization/master/tree/2015-street-tree-census.csv')
df_raw = df_raw.loc[df_raw['borocode'] == 1]
df_raw = df_raw.groupby('spc_common').size().reset_index(name='counts')
df_raw.sort_values(by=['counts'], ascending=False, inplace=True)
df_raw.reset_index(drop=True, inplace=True)
df = df_raw.loc[0:7]
df = df.append({'spc_common':'others','counts':df_raw['counts'].sum() - df_raw.loc[0:7]['counts'].sum()}, ignore_index=True)

font_file = os.path.abspath('~\tree.ttf')

plt.style.use('seaborn-whitegrid')
sns.set_style("white")

fig = plt.figure(
    FigureClass=Waffle,
    rows=7,
    columns=34,
    values=df['counts'],
    title={'label': 'What are some most common trees in New York, NY?', 'loc': 'left', 'fontdict': {'fontsize': 20}, 'y':1.05, 'color':'#3A3A3A'},
    labels=["{1}".format(n[0], n[1].title()) for n in df.itertuples()],
    legend={'loc': 'upper left', 'bbox_to_anchor': (1.03, 1.03), 'fontsize': 12},
    colors=['#32CD32','#C9FF81','#FAF207','#FF7903','#B1FF29','#35F007','#FF3C00','#228B22','#D0D0D0'],
    figsize=(13,8),
    icons='tree',
    font_size=20
)

plt.savefig('tree-pictogram.png')