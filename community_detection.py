### Author: Charles Stoksik
### Special thanks to the iGraph Foundation for their implementations of community detection algorithms
### Monday December 14, 2020

### Calling this program creates a csv with all the community detection encodings. These encodings can be used for analysis and visualization.

from igraph import Graph
from igraph import ARPACKOptions
import math
import numpy as np
import pandas as pd

### Load the Data ###
codes = pd.read_csv('output/community_detection/community_detection_encodings_output.csv', delimiter=',')
df = pd.read_csv('data/dij_joint_civ.csv') # original data
df['positive_Dij'] = [pow(math.e,d) for d in df['D_ij']] # column e^(original weight)
#codes.dropna(inplace=True)

### Build the dataframe ###
df5 = df[df['i'].isin(codes['Code'])]
df5 = df5[df5['j'].isin(codes['Code'])]
codes.set_index('Code', inplace=True)
#codes.dropna(inplace=True)

### Create the Graph ###
G = Graph()
G.add_vertices(list(set(df5['i'])) + ['ZW'])
for i, row in df5.iterrows():
    G.add_edge(row['i'], row['j'], weight=row['positive_Dij'])

### Fastgreedy Algorithm ###
partition = G.community_fastgreedy(weights='weight')
partition = partition.as_clustering()
groups = {}
for i, g in enumerate(partition.subgraphs()):
    for n in g.vs['name']:
        groups[n] = i
codes['fg'] = 0
for k, v in groups.items():
    codes.loc[k, 'fg'] = v
        
### Spinglass Algorithm ###
partition = G.community_spinglass(weights='weight')
#partition = partition.as_clustering()
groups = {}
for i, g in enumerate(partition.subgraphs()):
    for n in g.vs['name']:
        groups[n] = i
codes['sg'] = 0
for k, v in groups.items():
    codes.loc[k, 'sg'] = v
    
### Louvain Algorithm ###
partition = G.community_multilevel(weights='weight')
#partition = partition.as_clustering()
groups = {}
for i, g in enumerate(partition.subgraphs()):
    for n in g.vs['name']:
        groups[n] = i
codes['ml'] = 0
for k, v in groups.items():
    codes.loc[k, 'ml'] = v
    
### Leading Eigenvector with 2 Clusters ###
partition = G.community_leading_eigenvector(clusters=2, weights='weight', arpack_options=ARPACKOptions(max_iter=10000))
#partition = partition.as_clustering()
groups = {}
for i, g in enumerate(partition.subgraphs()):
    for n in g.vs['name']:
        groups[n] = i       
codes['le2'] = 0
for k, v in groups.items():
    codes.loc[k, 'le2'] = v
    
### Leading Eigenvector with 3 Clusters ###
partition = G.community_leading_eigenvector(clusters=3, weights='weight', arpack_options=ARPACKOptions(max_iter=10000))
#partition = partition.as_clustering()
groups = {}
for i, g in enumerate(partition.subgraphs()):
    for n in g.vs['name']:
        groups[n] = i
codes['le3'] = 0
for k, v in groups.items():
    codes.loc[k, 'le3'] = v
    
### Leading Eigenvector with 4 Clusters ###
partition = G.community_leading_eigenvector(clusters=4, weights='weight', arpack_options=ARPACKOptions(max_iter=10000))
#partition = partition.as_clustering()
groups = {}
for i, g in enumerate(partition.subgraphs()):
    for n in g.vs['name']:
        groups[n] = i        
codes['le4'] = 0
for k, v in groups.items():
    codes.loc[k, 'le4'] = v
    
### Leading Eigenvector with 8 Clusters ###
partition = G.community_leading_eigenvector(clusters=8, weights='weight', arpack_options=ARPACKOptions(max_iter=10000))
#partition = partition.as_clustering()
groups = {}
for i, g in enumerate(partition.subgraphs()):
    for n in g.vs['name']:
        groups[n] = i        
codes['le8'] = 0
for k, v in groups.items():
    codes.loc[k, 'le8'] = v
    

codes.to_csv('output/community_detection/community_detection_encodings_output.csv')