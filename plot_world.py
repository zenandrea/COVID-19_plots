#!/usr/bin/env python
# coding: utf-8

# # COVID-19 world
#
# https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
#
# https://github.com/CSSEGISandData/COVID-19

# In[1]:


import sys
#sys.path.append('/usr/local/lib/python3.7/site-packages')
sys.path


# In[2]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from datetime import datetime
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator


# In[3]:


#csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv
#url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
dati = pd.read_csv(url)

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
datid = pd.read_csv(url)


# In[4]:


dati.tail()


# In[5]:


dati.columns


# In[6]:


#dati.describe()
dati.index


# In[7]:


a = dati[ dati['Country/Region'] == 'US' ]
len( list( a['Province/State'] ) )
#print(a)
#type(a
a.sum()


# In[8]:


b = dati[ dati['Province/State'] == 'Hubei' ].T['1/22/20':].index
dati.T['1/22/20':].index
y = dati[ dati['Province/State'] == 'Hubei' ].T['1/22/20':].T.stack().to_numpy()
xticks = dati.T['1/22/20':].index
x = np.arange( len(xticks) )
x, y


# In[9]:


datetime.strptime("1/22/20", '%m/%d/%y').strftime('%m %d')
#datetime.strptime(, '%m/%d/%y').strftime('%m %d')
xticks
#for date in list(xticks): print(datetime.strptime(date, '%m/%d/%y').strftime('%b %d'))


# In[10]:


##%matplotlib
#plt.rcParams['figure.figsize'] = [10, 8]

plt.close('all')
mpl.style.use('default') #'seaborn-white', ggplot
fig, ax = plt.subplots(2,1, figsize=(10,15))

xticks = dati.T['1/22/20':].index
fxticks = [ datetime.strptime(date, '%m/%d/%y').strftime('%b %d') for date in list(xticks) ]
x = np.arange( len(xticks) )

#lista = ['Italy', 'France', 'Germany', 'Spain', 'United Kingdom']
lista = []
lista.append('China')
lista.append('Italy')
lista.append('US')
lista.append('Spain')
lista.append('Germany')
lista.append('Iran')
lista.append('France')
lista.append('Switzerland')
lista.append('Korea, South')
lista.append('United Kingdom')
lista.append('Netherlands')
lista.append('Austria')
lista.append('Belgium')
lista.append('Norway')
lista.append('Canada')

lista.append('Japan')
lista.append('Singapore')
lista.append('Brazil')
lista.append('Australia')
lista.append('India')
lista.append('Russia')

for name in lista:
#    print(name)
    y  = dati[ dati['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
    yd = datid[ datid['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
#    print(y)
    print(name,y[-1])
    ax[0].plot(x, y,
             marker = '.',
             linestyle = ':',
             label = name )
    ax[1].plot(x, yd,
             marker = '.',
             linestyle = ':',
             label = name )
    ax[0].set_ylabel('Confirmed')
    ax[1].set_ylabel('Deaths')

lista = []
#lista = ['Hubei', 'Beijing', 'New York']
for name in lista:
    print(name)
    y = dati[ dati['Province/State'] == name ].T['1/22/20':].T.stack().to_numpy()
    ax[0].plot(x, y,
               marker = '.',
               linestyle ='-.',
               label = name)
    ax[1].plot(x, yd,
               marker = '.',
               linestyle ='-.',
               label = name)

start = 5; step = 7
for i in range(2):
    #ax[i].set_xlim( 0, xt.max()+1)
    ax[i].set_xticks(x[start::step])
    ax[i].set_xticklabels(fxticks[start::step])
    #ax[i].set_xticklabels([])
    #ax[i].set_xticks(xticks, minor=True)
    ax[i].grid(True, 'both')
    ax[i].legend(loc='best')
    ax[i].set_ylim(bottom=8)
    ax[i].set_yscale('log')


#plt.axhline(y=50000,color='b', linestyle='-.')

#plt.savefig('plot_world.pdf')
plt.savefig('plot_world.png')


# In[11]:


##%matplotlib
#plt.rcParams['figure.figsize'] = [10, 8]

plt.close('all')
mpl.style.use('default') #'seaborn-white', ggplot
fig, ax = plt.subplots(2,1, figsize=(10,20))

xticks = dati.T['1/22/20':].index
fxticks = [ datetime.strptime(date, '%m/%d/%y').strftime('%b %d') for date in list(xticks) ]
x = np.arange( len(xticks) )

#lista = ['Italy', 'France', 'Germany', 'Spain', 'United Kingdom']
lista = []
lista.append('China')
lista.append('Italy')
lista.append('US')
lista.append('Spain')
lista.append('Germany')
lista.append('Iran')
lista.append('France')
lista.append('Switzerland')
lista.append('Korea, South')
lista.append('United Kingdom')
lista.append('Netherlands')
lista.append('Austria')
lista.append('Belgium')
lista.append('Norway')
lista.append('Canada')

lista.append('Japan')
lista.append('Singapore')
lista.append('Brazil')
lista.append('Australia')
lista.append('India')
lista.append('Russia')

xmin = 1; xmax = 10;
delay = 7 # days
print('delay = ',delay)

for name in lista:
#    print(name)
    y  = dati[ dati['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
    yd = datid[ datid['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
#    print(y)
    print(name,y[-1],yd[-1])
    ax[0].plot(y, yd,
             marker = 'o',
             linestyle = ':',
             label = name )
    ax[0].set_xlabel('Confirmed')
    ax[0].set_ylabel('Deaths')
    xmax = max( xmax, max(y) )
    # same plot with delay
    xn = y[:-delay]
    yn = yd[delay:]
    ii = np.logical_and( xn>1 , yn>1 )
    #print( len(xn[ii]) , len(yn[ii]) )
    ax[1].plot( xn[ii] , yn[ii],
             marker = '.',
             linestyle = ':',
             label = name )
    ax[1].set_xlabel('Confirmed')
    ax[1].set_ylabel('Deaths')
    ax[1].annotate( name, (xn[-1],yn[-1]), rotation=45 )

xlin = np.linspace( xmin, xmax )
for an in range(6):
    a = 0.02*an
    ax[0].plot( xlin, a*xlin, 'b--', alpha=0.3, label='' )
    ax[0].annotate('y={}*x'.format(a), (xmax,a*xmax) )

xlin = np.linspace( 1, xmax )
for an in range(1,7):
    a = 0.05*an
    ax[1].plot( xlin, a*xlin, '--', alpha=0.3, label='y={:3.2}*x'.format(a) )
    #ax[1].annotate('y={:3.2}*x'.format(a), (100, a*100), rotation=45 )

start = 5; step = 7
for i in range(2):
    #ax[i].set_xlim( 0, xt.max()+1)
    #ax[i].set_xticks(x[start::step])
    #ax[i].set_xticklabels(fxticks[start::step])
    #ax[i].set_xticklabels([])
    #ax[i].set_xticks(xticks, minor=True)
    ax[i].grid(True, 'both')
    ax[i].legend(loc='best')
    #ax[i].set_xlim(right=1e4)
    #ax[i].set_ylim(top=1e4)

ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[i].set_ylim(1)

plt.savefig('plot_world_scatter.png')


# In[12]:


##%matplotlib
#plt.rcParams['figure.figsize'] = [10, 8]

plt.close('all')
mpl.style.use('default') #'seaborn-white', ggplot
fig, ax = plt.subplots(1, 2, figsize=(15,8))

xticks = dati.T['1/22/20':].index
fxticks = [ datetime.strptime(date, '%m/%d/%y').strftime('%b %d') for date in list(xticks) ]
x = np.arange( len(xticks) )

#lista = ['Italy', 'France', 'Germany', 'Spain', 'United Kingdom']
lista = []
lista.append('China')
lista.append('Italy')
lista.append('US')
lista.append('Spain')
lista.append('Germany')
lista.append('Iran')
lista.append('France')
lista.append('Switzerland')
lista.append('Korea, South')
lista.append('United Kingdom')
#lista.append('Netherlands')
#lista.append('Austria')
#lista.append('Belgium')
#lista.append('Norway')
#lista.append('Canada')

#lista.append('Japan')
#lista.append('Singapore')
lista.append('Brazil')
#lista.append('Australia')
lista.append('India')
lista.append('Russia')

xmin = 1; xmax = 10;

delay = 7 # days
print('delay = ',delay)

for n, name in enumerate(lista):
    cn='C{}'.format(n)

#    print(name)
    y  = dati[ dati['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
    yd = datid[ datid['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
#    print(y)
    print(name,y[-1],yd[-1])
    yp = y>0
#    print( yp )
#    print( yd[yp] )
#    print( y[yp] )
    ax[0].plot(y[yp], yd[yp]/y[yp], label = name,
             marker = '.', linestyle = ':', color = cn )
    ax[0].set_xlabel('Confirmed')
    ax[0].set_ylabel('Deaths / Confirmed')
    ax[0].annotate( name, xy=(y[-1],yd[-1]/y[-1]), xycoords='data',
                       xytext=(30, 10), textcoords='offset points',
                       arrowprops=dict(facecolor='black',arrowstyle="->"),
                       horizontalalignment='left', verticalalignment='top', color=cn)

    # same plot with delay
    xn = y[:-delay]
    yn = yd[delay:]
    ii = np.logical_and( xn>1 , yn>1 )
    #print( len(xn[ii]) , len(yn[ii]) )
    ax[1].plot( xn[ii] , yn[ii] / xn[ii], label = name,
             marker = '.', linestyle = ':', color = cn )
    ax[1].set_xlabel('Confirmed')
    ax[1].set_ylabel('Deaths / Confirmed (delay {} days) '.format(delay) )
    ax[1].annotate( name, xy=(xn[-1],yn[-1]/xn[-1]), xycoords='data',
                       xytext=(30, 10), textcoords='offset points',
                       arrowprops=dict(facecolor='black',arrowstyle="->"),
                       horizontalalignment='left', verticalalignment='top', color=cn, rotation=0)


#xlin = np.linspace( xmin, xmax )
#for an in range(6):
#    a = 0.02*an
#    ax[0].plot( xlin, a+np.zeros(len(xlin)) , 'b--', alpha=0.3, label='' )
#    ax[0].annotate('y={}*x'.format(a), (xmax,a*xmax) )

xlin = np.linspace( 1, 1e5 )
for an in range(1,7):
    a = 0.02*an
    ax[1].plot( xlin, a+np.zeros(len(xlin)), '--', alpha=0.3, label='y={:3.2}*x'.format(a) )

#start = 5; step = 7
for i in range(2):
    #ax[i].set_xlim( 0, xt.max()+1)
    #ax[i].set_xticks(x[start::step])
    #ax[i].set_xticklabels(fxticks[start::step])
    #ax[i].set_xticklabels([])
    #ax[i].set_xticks(xticks, minor=True)
    ax[i].grid(True)
    ax[i].set_ylim(0.0,0.3)
    ax[i].set_xscale('log')
    ax[i].set_yscale('linear')

ax[0].legend(loc='best')

plt.savefig('plot_world_fatality.png')


# In[13]:


##%matplotlib
#plt.rcParams['figure.figsize'] = [10, 8]

plt.close('all')
mpl.style.use('default') # seaborn-white, ggplot, default
fig, ax = plt.subplots( 2,1, figsize=(10,20))

xticks = dati.T['1/22/20':].index
fxticks = [ datetime.strptime(date, '%m/%d/%y').strftime('%b %d') for date in list(xticks) ]
x = np.arange( len(xticks) )

#lista = ['Italy', 'France', 'Germany', 'Spain', 'United Kingdom']
lista = []
lista.append('China')
lista.append('Italy')
lista.append('US')
lista.append('Spain')
lista.append('Germany')
lista.append('Iran')
lista.append('France')
lista.append('Switzerland')
lista.append('Korea, South')
lista.append('United Kingdom')
lista.append('Netherlands')
lista.append('Austria')
lista.append('Belgium')
lista.append('Norway')
lista.append('Sweden')
lista.append('Canada')

lista.append('Japan')
lista.append('Singapore')
lista.append('Brazil')
lista.append('Australia')
lista.append('India')
lista.append('Russia')

deaths_xzero = 50

for n, name in enumerate(lista):
    cn='C{}'.format(n)
#    print(name)
    y  = dati[ dati['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
    yd = datid[ datid['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
#    print(y)
    print(name,y[-1],yd[-1])
    ax[0].plot(x, yd,
             marker = '.', linestyle = '--', color = cn,
             label = name )
    ax[0].annotate(name,
                       xy=( x[-1], yd[-1] ), xycoords='data',
                       #xytext=(0.8, 0.8-n*0.02), textcoords='axes fraction',
                       xytext=(30, 10), textcoords='offset points',
                       arrowprops=dict(facecolor='black',arrowstyle="->"),
                       horizontalalignment='left', verticalalignment='top', color=cn)

    xmax = max( xmax, max(y) )
    # same plot with delay
    try:
        delay = min( x[yd > deaths_xzero] )
        #delay = max( x[yd < deaths_xzero] )
        xn = x-delay
        #yn = yd[ xn>0 ]
        #xn = xn[ xn>0 ]
        ax[1].plot( xn , yd,
             marker = '.', linestyle = '--', color = cn,
             label = name )
        ax[1].annotate(name,
                       xy=( xn[-1], yd[-1] ), xycoords='data',
                       #xytext=(0.8, 0.8-n*0.02), textcoords='axes fraction',
                       xytext=(30, 10), textcoords='offset points',
                       arrowprops=dict(facecolor='black',arrowstyle="->"),
                       horizontalalignment='left', verticalalignment='top', color=cn)
    except:
        pass


start = 5; step = 7
#ax[0].set_xlabel('')
ax[0].set_ylabel('Deaths')
ax[0].set_xticks(x[start::step])
ax[0].set_xticklabels(fxticks[start::step])
ax[0].legend(loc='best')

ax[1].set_xlabel('Days from day with {} deaths'.format(deaths_xzero) )
ax[1].set_ylabel('Deaths')
ax[1].set_xlim( left=-1 )
ax[1].set_ylim( bottom=deaths_xzero )
#ax[1].set_xscale('log')
#ax[1].legend()

for i in range(2):
    #ax[i].set_xticks(x[start::step])
    #ax[i].set_xticklabels(fxticks[start::step])
    #ax[i].set_xticklabels([])
    #ax[i].set_xticks(xticks, minor=True)
    ax[i].grid(True, 'both')
    #ax[i].set_xlim(right=1e4)
    #ax[i].set_xscale('log')
    #ax[i].set_ylim(top=1e4)
    ax[i].set_yscale('log')


plt.savefig('plot_world_deaths.png')


# In[14]:


##%matplotlib
#plt.rcParams['figure.figsize'] = [10, 8]

plt.close('all')
mpl.style.use('default') # seaborn-white, ggplot, default
fig, ax = plt.subplots( 2,1, figsize=(10,20))

xticks = dati.T['1/22/20':].index
fxticks = [ datetime.strptime(date, '%m/%d/%y').strftime('%b %d') for date in list(xticks) ]
x = np.arange( len(xticks) )

#lista = ['Italy', 'France', 'Germany', 'Spain', 'United Kingdom']
lista = []
lista.append('China')
lista.append('Italy')
lista.append('US')
lista.append('Spain')
lista.append('Germany')
lista.append('Iran')
lista.append('France')
lista.append('Switzerland')
lista.append('Korea, South')
lista.append('United Kingdom')
lista.append('Netherlands')
lista.append('Austria')
lista.append('Belgium')
lista.append('Norway')
lista.append('Sweden')
lista.append('Canada')

lista.append('Japan')
lista.append('Singapore')
lista.append('Brazil')
lista.append('Australia')
lista.append('India')
lista.append('Russia')

y_xzero = 100

for n, name in enumerate(lista):
    cn='C{}'.format(n)
#    print(name)
    y  = dati[ dati['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
    yd = datid[ datid['Country/Region'] == name ].sum()['1/22/20':].to_numpy()
#    print(y)
    print(name,y[-1],yd[-1])
    ax[0].plot(x, y,
             marker = '.', linestyle = '--', color = cn,
             label = name )
    ax[0].annotate(name,
                       xy=( x[-1], y[-1] ), xycoords='data',
                       #xytext=(0.8, 0.8-n*0.02), textcoords='axes fraction',
                       xytext=(30, 10), textcoords='offset points',
                       arrowprops=dict(facecolor='black',arrowstyle="->"),
                       horizontalalignment='left', verticalalignment='top', color=cn)

    xmax = max( xmax, max(y) )
    # same plot with delay
    try:
        delay = min( x[y > y_xzero] )
        #delay = max( x[y < y_xzero] )
        xn = x-delay
        ax[1].plot( xn , y,
             marker = '.', linestyle = '--', color = cn,
             label = name )
        ax[1].annotate(name,
                       xy=( xn[-1], y[-1] ), xycoords='data',
                       #xytext=(0.8, 0.8-n*0.02), textcoords='axes fraction',
                       xytext=(30, 10), textcoords='offset points',
                       arrowprops=dict(facecolor='black',arrowstyle="->"),
                       horizontalalignment='left', verticalalignment='top', color=cn)

    except:
        pass


start = 5; step = 7
#ax[0].set_xlabel('')
ax[0].set_ylabel('Confirmed')
ax[0].set_xticks(x[start::step])
ax[0].set_xticklabels(fxticks[start::step])
ax[0].legend(loc='best')

ax[1].set_xlabel('Days from day with {} confirmed'.format(y_xzero) )
ax[1].set_ylabel('Confirmed')
ax[1].set_xlim( left=-1 )
ax[1].set_ylim( bottom=y_xzero )

for i in range(2):
    #ax[i].set_xticks(x[start::step])
    #ax[i].set_xticklabels(fxticks[start::step])
    #ax[i].set_xticklabels([])
    #ax[i].set_xticks(xticks, minor=True)
    ax[i].grid(True, 'both')
    #ax[i].set_xlim(right=1e4)
    #ax[i].set_xscale('log')
    #ax[i].set_ylim(top=1e4)
    ax[i].set_yscale('log')


plt.savefig('plot_world_confirmed.png')


# In[ ]:




