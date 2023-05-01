# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:27:02 2023

@author: abhinav.kumar
"""

import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import DBSCAN
from helping_functions.kmean_fx import create_table
from sklearn.tree import DecisionTreeClassifier
import plotly.express as px

def get_db_cluster(data, eps, min_s, stander):
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
    
    db = DBSCAN(eps=eps, min_samples=min_s).fit(dff)
    labels = db.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    df[f'cluster_{n_clusters_}'] = labels
    
    df = pd.concat([df_p[other_col], df], axis=1)
    cluster_list = [f'cluster_{n_clusters_}']
    cluster_list = pd.DataFrame(cluster_list, columns=['cluster']).to_dict('records')
    data['cluster_data'] = df.to_dict('records')
    data['cluster_list'] = cluster_list
    val = df[f'cluster_{n_clusters_}'].value_counts().to_frame()
    val = val.sort_index()
    val.reset_index(inplace=True, drop=False)
    val = val.rename(columns={'index':'Cluster'})
    val = create_table(val)
    return data, val

def getfeature_importance(data):
    cols = [i['row'] for i in data['model_selection']]
    cluster = [i['cluster'] for i in data['cluster_list']] 
    df = pd.DataFrame(data['cluster_data'])
    df = df.loc[df[cluster[0]] != -1]
    y = df.loc[:, cluster]
    X = df.loc[:, cols]
    tree = DecisionTreeClassifier().fit(X, y)
    importance = pd.DataFrame(tree.feature_importances_, index=X.columns).reset_index()
    importance = importance.rename(columns={'index':'Feature', 0:'importance'})
    importance = importance.sort_values('importance')
    fig = px.bar(importance, y='Feature', x='importance', orientation='h')
    fig.update_layout(
        plot_bgcolor="#fff",
        font=dict(color='#999999'),
        height=500,
        margin=dict(t=0, l=0, r=0, b=10, pad=0,autoexpand=True),
      )
    return fig
    