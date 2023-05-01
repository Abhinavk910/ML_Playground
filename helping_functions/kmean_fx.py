# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 01:32:08 2023

@author: abhinav.kumar
"""
from dash import html
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier

def create_table(df, textalign='center', minwidth='100px'):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col, style={'textAlign':textalign, 'minWidth':minwidth}) for col in columns])]
    rows = [html.Tr([html.Td(cell, style={'textAlign':textalign, 'minWidth':minwidth}) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table

def getheatmap(df, col='all', columns=[], title='Correlation Matrix'):
    if col != 'all':
        df = df[columns]
    if len(columns) < 7:
        height=500
    else:
        height=1000
    
    corr_matrix = df.corr()
    lower_half = corr_matrix.where(np.tril(np.ones(corr_matrix.shape), k=-1).astype(bool))
    fig = go.Figure(go.Heatmap(
        y=lower_half.index, x=lower_half.columns.tolist(), z=lower_half,texttemplate="%{z:.1f}",
                    textfont={"size":8},
        xgap=1, ygap=1, colorscale=[[0, 'red'], [0.5, 'white'], [1, 'green']], zmid=0, zmin=-1, zmax=1#[[0,'white'], [1, 'green']]
    ))
    fig.update_layout(
        plot_bgcolor="#fff",
        font=dict(color='#999999'),
        height=height,
        title="",
        margin=dict(t=10, l=10, r=10, b=10, pad=0)
      )
    fig.update_xaxes(tickangle=90)
    fig.update_traces(colorbar_orientation='h',
                      colorbar_len=0.26,
                      colorbar_thickness=15,
                      colorbar_title='Range',
                      colorbar=dict(titleside='top',titlefont=dict(size=14,family='Arial')),
                      colorbar_xanchor='right',
                      colorbar_xpad=0,colorbar_x=1,
                      colorbar_y=1.01,)
    return fig

def gethistogram(data, columns=[]):
    fig = px.histogram(data, x=columns, marginal='box')
    fig.update_layout(
            barmode='overlay',
            plot_bgcolor="#fff",
            font=dict(color='#999999'),
            height=500,
            title="",
            margin=dict(t=50, l=10, r=10, b=10, pad=0),
            legend=dict(orientation='h', y=1.1)
          )
    fig.update_traces(opacity=0.55)
    return fig

def gethist2d_fig(data, columns, title):
    fig = px.density_heatmap(data, x=columns[0],y = columns[1], 
                         marginal_x='box', marginal_y='box',
                         text_auto=True
                        )
    fig.update_layout(
            plot_bgcolor="#fff",
            font=dict(color='#999999'),
            height=500,
            title=title,
            margin=dict(t=50, l=50, r=10, b=50, pad=0,autoexpand=False),
            legend=dict(orientation='h', y=1.1),
            meta=dict(colorbar_orientation='h')
          )
    return fig

def getscatter_fig(data, columns, title):
    fig = px.scatter_matrix(data,dimensions=columns)
    fig.update_traces(showupperhalf=False, diagonal_visible=False)
    fig.update_layout(
            plot_bgcolor="#fff",
            font=dict(color='#999999'),
            height=500,
            title='',
            margin=dict(t=50, l=50, r=10, b=50, pad=0,autoexpand=True),
            legend=dict(orientation='h', y=1.1),
            meta=dict(colorbar_orientation='h')
          )
    return fig
    
def getelbow(data, value, n_cluster):
    columns = [i['row'] for i in data['model_selection']]
    df = pd.DataFrame(data['table'])[columns]
    df.dropna(inplace=True)
    
    if value == 'MinMax':
        df = preprocessing.MinMaxScaler().fit_transform(df)
    else:
        df = preprocessing.StandardScaler().fit_transform(df)
    inertia = [] 
    for i in range(1, n_cluster+1): 
        kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 2023)
        kmeans.fit(df) 
        inertia.append(kmeans.inertia_)

    fig = px.line(y=inertia, x=np.arange(1, len(inertia)+1))
    fig.update_traces(mode='lines+markers')
    fig.update_layout(plot_bgcolor='white')
    fig.update_yaxes(title='WCSS')
    fig.update_xaxes(title='Cluster')
    return fig

def create_model(data, value, stander):
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
    
    for clus in value:
        kmeans = KMeans(n_clusters = clus, init = "k-means++", random_state = 42)
        df[f'cluster_{clus}'] = kmeans.fit_predict(dff)
    
    df = pd.concat([df_p[other_col], df], axis=1)
    cluster_list = [f'cluster_{i}' for i in value]
    cluster_list = pd.DataFrame(cluster_list, columns=['cluster']).to_dict('records')
    data['cluster_data'] = df.to_dict('records')
    data['cluster_list'] = cluster_list
    
    dfinal=pd.DataFrame()
    for clus in value:
        dd = df.groupby([f'cluster_{clus}']).size().to_frame().reset_index()
        dd['cluster_group'] = f'cluster_{clus}'
        dd = dd.rename(columns={f'cluster_{clus}':'cluster', 0:'count'})
        dfinal = pd.concat([dfinal, dd])
    val = dfinal[['cluster_group', 'cluster', 'count']]    
    val = dfinal.pivot(index='cluster', columns='cluster_group', values='count').reset_index()
    val = create_table(val)
    return data, val

def blank_fig():
    fig = go.Figure(go.Scatter(x=[], y = []))
    fig.update_layout(template = None)
    fig.update_xaxes(showgrid = False, showticklabels = False, zeroline=False)
    fig.update_yaxes(showgrid = False, showticklabels = False, zeroline=False)
    
    return fig

def get_data_initial(df):
    table = df.to_dict('records')
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    n_df = df[numeric_cols]
    dd = n_df.describe().T#
    dd['Median'] = n_df.median()
    dd['Mode'] = n_df.mode().iloc[0]
    dd['Range'] = n_df.apply(lambda x:x.max() - x.min() if x.dtype != 'object' else '')
    dd['IQR'] = dd['75%'] - dd['25%']
    dd['Skew'] = n_df.skew()
    dd['Kurtosis'] = n_df.kurtosis()
    dd = dd.rename(columns={'count':'Count', 'mean':'Mean', 'std':'STD', 'min':'MIN', 'max':'MAX'})
    dd = dd[['Mean', 'Median', 'Mode', 'Range', 'IQR', 
       'STD', 'Skew', 'Kurtosis', 'MIN', '25%','50%',
       '75%', 'MAX', 'Count']]
    dd = round(dd.reset_index().rename(columns={'index':'Variables'}),3)
    table_data = dd.to_dict('records')

    col_data = dd.columns.tolist()[1:]
    col_data = pd.DataFrame(col_data, columns=['column']).to_dict('records')
    col_value = pd.DataFrame(['Mean', 'Median', 'Mode', 'MIN', 'MAX'], columns=['column_val']).to_dict('records')
    row_data_list = dd.Variables.unique().tolist()
    row_data = pd.DataFrame(row_data_list, columns=['row']).to_dict('records')
    
    model_selection=row_data
    if len(row_data_list)>10:
        new_row = pd.DataFrame(row_data_list[:5], columns=['row']).to_dict('records')
    else:
        new_row = pd.DataFrame(row_data_list, columns=['row']).to_dict('records')
    store_data = {'table':table, 'table_data': table_data, 'available_column':col_data,
      'available_column_val':col_value, 'available_row':row_data, 'model_selection':model_selection,'new_row':new_row}
    return store_data


def getboxplot(df,cluster, var, title='Correlation Matrix'):
    fig = px.box(df, x=cluster, y=var)
    fig.update_layout(
        plot_bgcolor="#fff",
        font=dict(color='#999999'),
        height=500,
        title=title,
        margin=dict(t=10, l=10, r=10, b=20, pad=0)
      )
    fig.update_xaxes(tickangle=0)
    return fig

def getscatterplot(data, columns, cluster, title):
    data[cluster] = data[cluster].apply(lambda x: f'c-{x}')
    fig = px.scatter_matrix(data,dimensions=columns, color=cluster, category_orders={cluster:[f'c-{x}' for x in np.arange(int(cluster.split('_')[-1]))]})
    fig.update_traces(showupperhalf=False, diagonal_visible=False)
    fig.update_layout(
            plot_bgcolor="#fff",
            font=dict(color='#999999'),
            height=500,
            title=title,
            margin=dict(t=50, l=50, r=10, b=50, pad=0,autoexpand=True),
            legend=dict(orientation='h', y=1.1),
            meta=dict(colorbar_orientation='h')
          )
    return fig

def get3dscatterplot(data, columns, cluster, title):
    data[cluster] = data[cluster].apply(lambda x: f'c-{x}')
    x, y, z = columns
    fig = px.scatter_3d(data,x=x,y=y,z=z, color=cluster, category_orders={cluster:[f'c-{x}' for x in np.arange(int(cluster.split('_')[-1]))]})
    fig.update_layout(
            plot_bgcolor="#fff",
            font=dict(color='#999999'),
            height=500,
            title=title,
            margin=dict(t=0, l=0, r=0, b=0, pad=0,autoexpand=True),
            legend=dict(orientation='h', y=1.1),
          )
    return fig

def getfeature_importance(data, cluster):
    cols = [i['row'] for i in data['model_selection']] 
    df = pd.DataFrame(data['cluster_data'])
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