# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:50:21 2023

@author: abhinav.kumar
"""
import plotly.figure_factory as ff
import pandas as pd
from sklearn import preprocessing
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import AgglomerativeClustering
from helping_functions.kmean_fx import create_table

def get_dendrogram(data, value):
    columns = [i['row'] for i in data['model_selection']]
    df = pd.DataFrame(data['table'])[columns]
    df.dropna(inplace=True)
    
    if value == 'MinMax':
        df = preprocessing.MinMaxScaler().fit_transform(df)
    else:
        df = preprocessing.StandardScaler().fit_transform(df)
        
    D = pdist(df)

    Z = linkage(D)
    fig = ff.create_dendrogram(Z)
    fig.update_xaxes(showticklabels=False, fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    fig.update_layout(plot_bgcolor='white')
    
    return fig

def get_hierarchical_cluster(data, cluster, stander):
    cols = [i['row'] for i in data['model_selection']]
    df_p = pd.DataFrame(data['table'])
    df_p.dropna(inplace=True)
    df_p.reset_index(inplace=True, drop=True)
    df = df_p[cols]
    other_col=[i for i in df_p.columns if i not in cols]
    if stander == 'MinMax':
        dff = preprocessing.MinMaxScaler().fit_transform(df)
    else:
        dff = preprocessing.StandardScaler().fit_transform(df)
    
    for clus in cluster:
        agglo = AgglomerativeClustering(n_clusters=int(clus), affinity='euclidean', linkage='ward')  
        df[f'cluster_{clus}'] =  agglo.fit_predict(dff)
    
    df = pd.concat([df_p[other_col], df], axis=1)
    cluster_list = [f'cluster_{i}' for i in cluster]
    cluster_list = pd.DataFrame(cluster_list, columns=['cluster']).to_dict('records')
    data['cluster_data'] = df.to_dict('records')
    data['cluster_list'] = cluster_list
    
    dfinal=pd.DataFrame()
    for clus in cluster:
        dd = df.groupby([f'cluster_{clus}']).size().to_frame().reset_index()
        dd['cluster_group'] = f'cluster_{clus}'
        dd = dd.rename(columns={f'cluster_{clus}':'cluster', 0:'count'})
        dfinal = pd.concat([dfinal, dd])
    val = dfinal[['cluster_group', 'cluster', 'count']]    
    val = dfinal.pivot(index='cluster', columns='cluster_group', values='count').reset_index()
    val = create_table(val)
    return data, val