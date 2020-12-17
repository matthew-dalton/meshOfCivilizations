import math
import numpy as np
import networkx as nx
import networkx.algorithms.community as nx_comm
import pandas as pd

Asia_List = ['AE', 'AZ', 'BD', 'CN', 'ID', 'IL', 'IN', 'JO', 'JP', 'KH',
             'KR', 'KZ', 'LA', 'LK', 'MY', 'NP', 'PH', 'PK', 'SA', 'SG',
             'TH', 'TR', 'UZ', 'VN', 'YE']
Africa_List = ['AO', 'BF', 'BI', 'CI', 'CM', 'DZ', 'EG', 'ET', 'GH',
               'KE', 'MA', 'MG', 'ML', 'MZ', 'NG', 'SD', 'SN', 'TN', 'ZA',
               'ZM', 'ZW']
Australia_List = ['AU', 'PG']
Europe_List = ['AT', 'BE', 'BG', 'BY', 'CH', 'CZ', 'DE', 'DK', 'ES', 'FI',
               'FR', 'GB', 'GR', 'HU', 'IT', 'NL', 'PL', 'PT', 'RU',
               'SE', 'SK', 'UA']
NA_List = ['CA', 'DO', 'GT', 'HN', 'HT', 'MX', 'NI', 'SV', 'US']
SA_List = ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'PE', 'PY', 'VE']


Both_List = ['CH', 'ID', 'IN', 'TR']
G20_List = ['AR', 'AU', 'BR', 'CA', 'DE', 'FR', 'GB', 'IT', 'JP', 'KR',
            'MX', 'RU', 'SA', 'US', 'ZA']
G33_List = ['CI', 'DO', 'GT', 'HN', 'HT', 'KE', 'LA', 'LK', 'MG', 'NG',
            'NI', 'PH', 'PK', 'SN', 'SV', 'VE', 'ZM', 'ZW']
Neither_List = ['AE', 'AO', 'AT', 'AZ', 'BD', 'BE', 'BF', 'BG', 'BI', 'BO',
                'BY', 'CL', 'CM', 'CN', 'CO', 'CZ', 'DK', 'DZ', 'EC', 'EG',
                'ES', 'ET', 'FI', 'GH', 'GR', 'HU', 'IL', 'JO', 'KH', 'KZ',
                'MA', 'ML', 'MY', 'MZ', 'NL', 'NP', 'PE', 'PG', 'PL', 'PT',
                'PY', 'SD', 'SE', 'SG', 'SK', 'TH', 'TN', 'UA', 'UZ', 'VN',
                'YE']

# codes = pd.read_csv('data/codes.csv')
fivemillioncodes = pd.read_csv('/Users/mattreyes/Desktop/codes5mlle.csv')
df = pd.read_csv('/Users/mattreyes/Desktop/dij_joint_civ.csv')

five_mil_codelist = []
for index, row in fivemillioncodes.iterrows():
    five_mil_codelist.append((row['Code']))

# transformed values by exponential, filters list by countries with over 5 mil population
filtered_list = []
for index, row in df.iterrows():
    if row['i'] in five_mil_codelist and row['j'] in five_mil_codelist:
        filtered_list.append((row['i'], row['j'], {'weight': math.exp(row['D_ij'])}))

H = nx.Graph()

H.add_nodes_from(Asia_List, Continent='Asia')
H.add_nodes_from(Africa_List, Continent='Africa')
H.add_nodes_from(Australia_List, Continent='Australia')
H.add_nodes_from(Europe_List, Continent='Europe')
H.add_nodes_from(NA_List, Continent='NA')
H.add_nodes_from(SA_List, Continent='SA')

H.add_edges_from(filtered_list)

I = nx.Graph()

I.add_nodes_from(Both_List, Affil='Both')
I.add_nodes_from(G20_List, Affil='G20')
I.add_nodes_from(G33_List, Affil='G33')
I.add_nodes_from(Neither_List, Affil='Neither')

I.add_edges_from(filtered_list)

cont_mod = nx_comm.modularity(H, [Asia_List, Africa_List, Australia_List, Europe_List, NA_List, SA_List], weight='weight')
print('Q1 = ', cont_mod)

aff_mod = nx_comm.modularity(I, [Both_List, G20_List, G33_List, Neither_List], weight='weight')
print('Q2 = ', aff_mod)

cont_assort = nx.attribute_assortativity_coefficient(H, 'Continent')
print('r1 = ', cont_assort)

aff_assort = nx.attribute_assortativity_coefficient(I, 'Affil')
print('r2 = ', aff_assort)
