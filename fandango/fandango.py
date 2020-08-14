import pandas as pd
import seaborn as sns; sns.set()
import matplotlib
import matplotlib.pyplot as plt

"""
uses columns of normalized rating values rounded to the nearest half star in the dataset
columns that end with _norm_round are such columns
"""

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/fandango/fandango_score_comparison.csv')

df = df[['FILM','RT_norm_round', 'RT_user_norm_round',
        'Metacritic_norm_round', 'Metacritic_user_norm_round',
        'IMDB_norm_round','Fandango_Stars']]

RT_norm_round = df.groupby(by=['RT_norm_round']).count()
RT_norm_round = RT_norm_round.filter(['FILM'])
RT_norm_round.rename(columns={'FILM':'count'}, inplace=True)
RT_norm_round.index.rename('rating', inplace=True)
RT_norm_round.reset_index(inplace=True)
pl = []
for i in range(len(RT_norm_round)):
    num = round(RT_norm_round['count'].to_list()[i] / RT_norm_round['count'].sum() * 100, 2)
    pl.append(num)
RT_norm_round['percentage'] = pl

RT_user_norm_round = df.groupby(by=['RT_user_norm_round']).count()
RT_user_norm_round = RT_user_norm_round.filter(['FILM'])
RT_user_norm_round.rename(columns={'FILM':'count'}, inplace=True)
RT_user_norm_round.index.rename('rating', inplace=True)
RT_user_norm_round.reset_index(inplace=True)
pl = []
for i in range(len(RT_user_norm_round)):
    num = round(RT_user_norm_round['count'].to_list()[i] / RT_user_norm_round['count'].sum() * 100, 2)
    pl.append(num)
RT_user_norm_round['percentage'] = pl

Metacritic_norm_round = df.groupby(by=['Metacritic_norm_round']).count()
Metacritic_norm_round = Metacritic_norm_round.filter(['FILM'])
Metacritic_norm_round.rename(columns={'FILM':'count'}, inplace=True)
Metacritic_norm_round.index.rename('rating', inplace=True)
Metacritic_norm_round.reset_index(inplace=True)
pl = []
for i in range(len(Metacritic_norm_round)):
    num = round(Metacritic_norm_round['count'].to_list()[i] / Metacritic_norm_round['count'].sum() * 100, 2)
    pl.append(num)
Metacritic_norm_round['percentage'] = pl

Metacritic_user_norm_round = df.groupby(by=['Metacritic_user_norm_round']).count()
Metacritic_user_norm_round = Metacritic_user_norm_round.filter(['FILM'])
Metacritic_user_norm_round.rename(columns={'FILM':'count'}, inplace=True)
Metacritic_user_norm_round.index.rename('rating', inplace=True)
Metacritic_user_norm_round.reset_index(inplace=True)
pl = []
for i in range(len(Metacritic_user_norm_round)):
    num = round(Metacritic_user_norm_round['count'].to_list()[i] / Metacritic_user_norm_round['count'].sum() * 100, 2)
    pl.append(num)
Metacritic_user_norm_round['percentage'] = pl

IMDB_norm_round = df.groupby(by=['IMDB_norm_round']).count()
IMDB_norm_round = IMDB_norm_round.filter(['FILM'])
IMDB_norm_round.rename(columns={'FILM':'count'}, inplace=True)
IMDB_norm_round.index.rename('rating', inplace=True)
IMDB_norm_round.reset_index(inplace=True)
pl = []
for i in range(len(IMDB_norm_round)):
    num = round(IMDB_norm_round['count'].to_list()[i] / IMDB_norm_round['count'].sum() * 100, 2)
    pl.append(num)
IMDB_norm_round['percentage'] = pl

fandango = df.groupby(by=['Fandango_Stars']).count()
fandango = fandango.filter(['FILM'])
fandango.rename(columns={'FILM':'count'}, inplace=True)
fandango.index.rename('rating', inplace=True)
fandango.reset_index(inplace=True)
pl = []
for i in range(len(fandango)):
    num = round(fandango['count'].to_list()[i] / fandango['count'].sum() * 100, 2)
    pl.append(num)
fandango['percentage'] = pl

rating0h = pd.DataFrame({'rating':0.5, 'count':0, 'percentage':0}, index=[0])
rating1 = pd.DataFrame({'rating':1, 'count':0, 'percentage':0}, index=[0])
rating1h = pd.DataFrame({'rating':1.5, 'count':0, 'percentage':0}, index=[0])
rating2 = pd.DataFrame({'rating':2, 'count':0, 'percentage':0}, index=[0])
rating2h = pd.DataFrame({'rating':2.5, 'count':0, 'percentage':0}, index=[0])
rating5 = pd.DataFrame({'rating':5, 'count':0, 'percentage':0}, index=[0])

IMDB_norm_round = IMDB_norm_round.append(rating1h, ignore_index=True)
IMDB_norm_round = IMDB_norm_round.append(rating1, ignore_index=True)
IMDB_norm_round = IMDB_norm_round.append(rating0h, ignore_index=True)
IMDB_norm_round = IMDB_norm_round.append(rating5, ignore_index=True)
IMDB_norm_round.sort_values(by='rating', inplace=True)
IMDB_norm_round.reset_index(drop=True, inplace=True)

Metacritic_norm_round = Metacritic_norm_round.append(rating5, ignore_index=True)
Metacritic_norm_round.sort_values(by='rating', inplace=True)
Metacritic_norm_round.reset_index(drop=True, inplace=True)

Metacritic_user_norm_round = Metacritic_user_norm_round.append(rating0h, ignore_index=True)
Metacritic_user_norm_round.sort_values(by='rating', inplace=True)
Metacritic_user_norm_round.reset_index(drop=True, inplace=True)

RT_user_norm_round = RT_user_norm_round.append(rating0h, ignore_index=False)
RT_user_norm_round = RT_user_norm_round.append(rating5, ignore_index=False)
RT_user_norm_round.sort_values(by='rating', inplace=True)
RT_user_norm_round.reset_index(drop=True, inplace=True)

fandango = fandango.append(rating0h, ignore_index=False)
fandango = fandango.append(rating1, ignore_index=False)
fandango = fandango.append(rating1h, ignore_index=False)
fandango = fandango.append(rating2, ignore_index=False)
fandango = fandango.append(rating2h, ignore_index=False)
fandango.sort_values(by='rating', inplace=True)
fandango.reset_index(drop=True, inplace=True)

sns.set_style("whitegrid")
ax = sns.lineplot(x='rating',y='percentage',data=IMDB_norm_round, color='#F9F10E')
sns.lineplot(x='rating',y='percentage',data=Metacritic_norm_round,ax=ax, color='#6495ED')
sns.lineplot(x='rating',y='percentage',data=Metacritic_user_norm_round,ax=ax, color='#3CB371')
sns.lineplot(x='rating',y='percentage',data=RT_norm_round,ax=ax, color='#808080')
sns.lineplot(x='rating',y='percentage',data=RT_user_norm_round,ax=ax, color='#BA55D3')
sns.lineplot(x='rating',y='percentage',data=fandango,ax=ax, color='#f4320c')
ax.set(xlim=(-.15, None))
sns.despine(bottom=True,left=True)
ax.set(xlabel='', ylabel='')
plt.plot([3.3, 2.9], [26, 27.5], linewidth=1, color='grey')
ax.text(3.05, 42, 'IMDB\nusers', color='#F2EA00', fontsize=9)
ax.text(4.15, 38.45, 'Fandango', color='#f4320c', fontsize=9)
ax.text(2.35, 27.1, 'Metacritic\n   users', color='#3CB371', fontsize=9)
ax.text(2.03, 16.7, '  Rotten\nTomatoes\n    users', color='#BA55D3', fontsize=9)
ax.text(1.15, 14.52, 'Metacritic', color='#6495ED', fontsize=9)
ax.text(0.15, 10.5, '  Rotten\nTomatoes', color='#808080', fontsize=9)
matplotlib.rcParams['font.sans-serif'] = ['Source Han Sans TW', 'sans-serif']
ax.set_xticklabels(['','☆','★','★★','★★★','★★★★','★★★★★'])
ax.set_yticklabels(['','0','10','20','30','40%'], fontsize=9.5)
ax.text(x=-.07, y=1.05, s='Normalized rating distribution of 146 films in 2015\nthat had 30+ reviews on Fandango.com',
        fontsize=12.4, ha='left', va='bottom', transform=ax.transAxes)
plt.savefig('fandango-loves-movies.png')
