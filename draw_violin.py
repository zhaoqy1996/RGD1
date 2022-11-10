import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
df = pd.read_csv('DFT_reaction_info.csv')
info = pd.read_csv('Freaction_features.csv')
df['break'] = info['N_bond_break']
df['diff']  = info['N_bond_break'] - info['N_bond_form']
df = df.drop(columns=['type','DE_F_xTB','DE_B_xTB','DF_F','DF_B'])
df = df[df['break']<=5]
max_DG = df[["DE_F", "DE_B"]].max(axis=1)
min_DG = df[["DE_F", "DE_B"]].min(axis=1)

newdf = pd.concat([df,df],ignore_index=True)
newdf['DE'] = pd.concat([max_DG,min_DG],ignore_index=True) 
newdf['Etype'] = ['max']*len(df)+['min']*len(df)

ax = sns.violinplot(x="break", y="DE", data=newdf, palette="Paired", hue="Etype", split=True, scale="width", cut=0, inner='quartile')

plt.savefig('DEDH_dist.pdf', bbox_inches = 'tight', dpi=600)
