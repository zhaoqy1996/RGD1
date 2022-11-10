import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load in data
data = pd.read_csv('Freaction_features.csv')
df   = data.drop(['Rindex'],axis=1)
#df   = df.drop_duplicates()

fig = plt.figure(figsize=(15, 14))

ax1 = plt.subplot2grid(shape=(3, 6), loc=(0, 0), colspan=3)
ax2 = plt.subplot2grid(shape=(3, 6), loc=(0, 3), colspan=3)
ax3 = plt.subplot2grid(shape=(3, 6), loc=(1, 0), colspan=2)
ax4 = plt.subplot2grid(shape=(3, 6), loc=(1, 2), colspan=2)
ax5 = plt.subplot2grid(shape=(3, 6), loc=(1, 4), colspan=2)
ax6 = plt.subplot2grid(shape=(3, 6), loc=(2, 0), colspan=6)

# first count bond break and form
b1=df[df.N_bond_break==1]
b2=df[df.N_bond_break==2]
b3=df[df.N_bond_break==3]
b4=df[df.N_bond_break==4]
b5=df[df.N_bond_break==5]

Nreactions = [len(b1),len(b2[df.N_bond_form==1]),len(b2[df.N_bond_form==2]),len(b3[df.N_bond_form==2]),len(b3[df.N_bond_form==3]),len(b4),len(b5)]
index = ['b1','b2f1','b2f2','b3f2','b3f3','b4','b5']
rangea = list(range(1,len(index)+1)) 
ax1.vlines(x=rangea, ymin=0, ymax=Nreactions, color='#007ACC', alpha=0.25, linewidth=10)
ax1.plot(rangea,Nreactions, "o", markersize=8.5, color='#007ACC', alpha=0.6)
ax1.set_yscale('log')

# label for each coloum
csfont = {'fontname':'Arial','fontsize':15,'fontweight':'normal'}  
for cx,x in enumerate(rangea):
    height = Nreactions[cx]+3
    ax1.annotate('{}'.format(Nreactions[cx]),
                xy=(x, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom',**csfont)

# set lim
ax1.set_xlim(0.5, len(index)+0.5)
ax1.set_ylim(min(Nreactions)/5.0, max(Nreactions)*5)

# set labels
ax1.set_xlabel('Reaction type', fontsize=15, fontweight='black', color = '#333F4B', fontname='Arial')
ax1.set_ylabel('Number of reactions',fontsize=15, fontweight='black', color = '#333F4B', fontname='Arial')

# set axis
tickfont = {'fontname':'Arial','fontsize':16}
ax1.set_xticks(range(1,len(index)+1))
ax1.set_xticklabels(index,**tickfont)
ax1.tick_params(axis='y', labelsize=15)

#plt.yticks(np.arange(0, 100.1, 20),**tickfont)

# pannel 2
Nreactions = []
for NT in range(min(df.Nheavy),max(df.Nheavy)+1):
    Nreactions += [len(df[df.Nheavy==NT])]

index = list(range(min(df.Nheavy),max(df.Nheavy)+1))
rangeb = list(range(1,len(index)+1)) 
ax2.vlines(x=rangeb, ymin=0, ymax=Nreactions, color='#007ACC', alpha=0.25, linewidth=10)
ax2.plot(rangeb,Nreactions, "o", markersize=8.5, color='#007ACC', alpha=0.6)
ax2.set_yscale('log')

# label for each coloum
for cx,x in enumerate(rangeb):
    height = Nreactions[cx]+3
    ax2.annotate('{}'.format(Nreactions[cx]),
                xy=(x, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom',**csfont)

# set lim
ax2.set_xlim(0.5, len(index)+0.5)
ax2.set_ylim(min(Nreactions)/5.0, max(Nreactions)*5)

# set labels
ax2.set_xlabel('Number of heavy atoms', fontsize=15, fontweight='black', color = '#333F4B', fontname='Arial')
ax2.set_xticks(range(1,len(index)+1))
ax2.set_xticklabels(index,**tickfont)
ax2.tick_params(axis='y', labelsize=15)

# pannel 6
Nreactions = []
index = ['N_CC', 'N_CN', 'N_CO', 'N_CH', 'N_NN', 'N_NO', 'N_NH', 'N_OO', 'N_OH', 'N_HH']
for item in index:
    Nreactions += [df[item].sum()]

rangeg = list(range(1,len(index)+1)) 
ax6.vlines(x=rangeg, ymin=0, ymax=Nreactions, color='#007ACC', alpha=0.25, linewidth=10)
ax6.plot(rangeg,Nreactions, "o", markersize=8.5, color='#007ACC', alpha=0.6)
ax6.set_yscale('log')

# label for each coloum
for cx,x in enumerate(rangeg):
    height = Nreactions[cx]+3
    ax6.annotate('{}'.format(Nreactions[cx]),
                xy=(x, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom',**csfont)

# set lim
ax6.set_xlim(0.5, len(index)+0.5)
ax6.set_ylim(min(Nreactions)/5.0, max(Nreactions)*5)

# set labels
ax6.set_xlabel('bond change types', fontsize=15, fontweight='black', color = '#333F4B', fontname='Arial')
ax6.set_ylabel('Number of bonds',fontsize=15, fontweight='black', color = '#333F4B', fontname='Arial')
ax6.set_xticks(range(1,len(index)+1))
ax6.set_xticklabels(index,**tickfont)
ax6.tick_params(axis='y', labelsize=15)

# pannel 3-5
Nreactions = [df.L1_NC.sum(),df.L1_NN.sum(),df.L1_NO.sum(),df.L1_NH.sum()]
index      = ['C','N','O','H']
rangec = list(range(1,len(index)+1))

ax3.vlines(x=rangec, ymin=0, ymax=Nreactions, color='#007ACC', alpha=0.25, linewidth=10)
ax3.plot(rangec,Nreactions, "o", markersize=8.5, color='#007ACC', alpha=0.6)
ax3.set_yscale('log')

# label for each coloum
for cx,x in enumerate(rangec):
    height = Nreactions[cx]+3
    ax3.annotate('{}'.format(Nreactions[cx]),
                xy=(x, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom',**csfont)

# set lim
ax3.set_xlim(0.5, len(index)+0.5)
#ax3.set_ylim(min(Nreactions)/5.0, max(Nreactions)*5)
ax3.set_ylim(2000,5e6)

# set labels
ax3.set_xlabel('Number of reactive atoms', fontsize=15, fontweight='black', color = '#333F4B', fontname='Arial')
ax3.set_ylabel('Number of atoms',fontsize=15, fontweight='black', color = '#333F4B', fontname='Arial')
ax3.set_xticks(range(1,len(index)+1))
ax3.set_xticklabels(index,**tickfont)
ax3.tick_params(axis='y', labelsize=15)

# pannel 4
Nreactions = [df.L2_NC.sum(),df.L2_NN.sum(),df.L2_NO.sum(),df.L2_NH.sum()]
ax4.vlines(x=rangec, ymin=0, ymax=Nreactions, color='#007ACC', alpha=0.25, linewidth=10)
ax4.plot(rangec,Nreactions, "o", markersize=8.5, color='#007ACC', alpha=0.6)
ax4.set_yscale('log')

# label for each coloum
for cx,x in enumerate(rangec):
    height = Nreactions[cx]+3
    ax4.annotate('{}'.format(Nreactions[cx]),
                xy=(x, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom',**csfont)

# set lim
ax4.set_xlim(0.5, len(index)+0.5)
#ax4.set_ylim(min(Nreactions)/5.0, max(Nreactions)*5)
ax4.set_ylim(2000,5e6)

# set labels
ax4.set_xlabel('Number of nearest atoms', fontsize=15, fontweight='black', color = '#333F4B', fontname='Arial')
ax4.set_xticks(range(1,len(index)+1))
ax4.set_xticklabels(index,**tickfont)
ax4.tick_params(axis='y', labelsize=15)

# pannel 5
Nreactions = [df.L3_NC.sum(),df.L3_NN.sum(),df.L3_NO.sum(),df.L3_NH.sum()]
ax5.vlines(x=rangec, ymin=0, ymax=Nreactions, color='#007ACC', alpha=0.25, linewidth=10)
ax5.plot(rangec,Nreactions, "o", markersize=8.5, color='#007ACC', alpha=0.6)
ax5.set_yscale('log')

# label for each coloum
for cx,x in enumerate(rangec):
    height = Nreactions[cx]+3
    ax5.annotate('{}'.format(Nreactions[cx]),
                xy=(x, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom',**csfont)

# set lim
ax5.set_xlim(0.5, len(index)+0.5)
#ax5.set_ylim(min(Nreactions)/5.0, max(Nreactions)*5)
ax5.set_ylim(2000,5e6)

# set labels
ax5.set_xlabel('Number of next-nearest atoms', fontsize=15, fontweight='black', color = '#333F4B', fontname='Arial')
ax5.set_xticks(range(1,len(index)+1))
ax5.set_xticklabels(index,**tickfont)
ax5.tick_params(axis='y', labelsize=15)

plt.savefig('reaction_stat.pdf', dpi=600)
