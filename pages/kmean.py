# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 01:21:24 2023

@author: abhinav.kumar
"""

from dash import html, dcc, Input, Output, State, no_update
import dash
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import base64
import io
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import plotly.express as px
from helping_pages.kmean_hp import data_page1, data_page2, data_page3, data_page4
from helping_functions.kmean_fx import get_data_initial, create_table, getheatmap,gethistogram,gethist2d_fig, getscatter_fig, getelbow, create_model, getboxplot, getscatterplot, get3dscatterplot


dash.register_page(__name__)

min_step = 0
max_step = 4
active = 0

layout = html.Div([
        dcc.Store(id='used-data', data=None, storage_type='session'),
        dmc.Container(
            style={'backgroundColor':'whitesmoke','marginTop':'0.2rem','padding':'1rem',
                   'minHeight':'100vh', 'maxWidth':'1200px'},
            children=[
                dmc.Stepper(
                    id="stepper-basic-usage",
                    active=active,
                    size='xs',
                    contentPadding=1,
                    styles={'separator':{'margin':'0px'}},
                    children=[
                        dmc.StepperStep(
                            label="First step",
                            description="Load Data",
                            size='xs',
                            children=data_page1
                        ),
                        dmc.StepperStep(
                            label="Second step",
                            description="Data Cleaning",
                            id='step2',
                            children=data_page2
                        ),
                        dmc.StepperStep(
                            label="Third step",
                            description="Model Building",
                            children=data_page3
                        ),
                        dmc.StepperStep(
                            label="Final step",
                            description="View Cluster",
                            children=data_page4
                        ),
                        dmc.StepperCompleted(
                            children=[
                                dmc.Text(
                                    "Done!!!",
                                    align="center", weight=700, size=30
                                ),
                                dmc.Center(
                                    style={'marginTop':'20px'},
                                    children=[
                                        dmc.Button("Download xlsx", id="btn_xslx",
                                               leftIcon=DashIconify(icon="material-symbols:download-rounded"),
                                               style={'width':'200px', 'margin':'auto'}),
                                        dcc.Download(id="download_xslx")
                                    ]   
                                )
                            ]
                        ),
                    ],
                ),
                dmc.Group(
                    position="center",
                    mt="xl",
                    children=[
                        html.Div(
                            dmc.Button("Back", id="back-kmean", variant="default",leftIcon=DashIconify(icon="material-symbols:arrow-back")),
                            id='back-div',
                            hidden=False
                        ),
                        html.Div(
                            dmc.Button("Next step", id="next-kmean",variant='gradient', rightIcon=DashIconify(icon="material-symbols:arrow-forward")),
                            id='next-div',
                            hidden=False
                        )
                    ],
                ),
            ]
        )
    ]
)


##########################   callbacks   ######################################

# CB1 - handle stepper
dash.clientside_callback(
    """
    function(clicks1, clicks2, state) {
        var ctx = dash_clientside.callback_context;
        if (ctx.triggered.length > 0) {
            var prop_id = ctx.triggered[0]['prop_id'];
            if (prop_id === 'back-kmean.n_clicks') {
                if(state > 0){
                return state - 1;
                } else {
                    return state
                }
            } else if (prop_id === 'next-kmean.n_clicks') {
                if(state < 4){
                    return state + 1;
                } else {
                    return state
            }
            }
        }
        return "";
    }
    """,
    Output("stepper-basic-usage", "active"),
    Input("back-kmean", "n_clicks"),
    Input("next-kmean", "n_clicks"),
    State("stepper-basic-usage", "active"),
    prevent_initial_call=True
)
                
# CB25 - stepper button hide                  
dash.clientside_callback(
    """
    function(active) {
        if (active === 0) {
            return [false, true];
        } else if (active === 4) {
            return [true, false];
        } else {
            return [false, false];    
        }
    }
    """,
    Output("next-div", "hidden"),
    Output('back-div', 'hidden'),
    Input("stepper-basic-usage", "active")
)
                 
                    

#CB2 -  uploading table and storing
@dash.callback(Output('alert-check', 'hide'),Output('alert-check', 'color'),Output('alert-check', 'title'),Output('alert-check', 'children'),
              Output('alert-check2', 'hide'),Output('alert-check2', 'color'),Output('alert-check2', 'title'),Output('alert-check2', 'children'),
              Output('check1', 'value'),Output('table-data', 'children'),Output('table-data2', 'children'), Output('used-data', 'data'),
              Input('upload-data', 'contents'),
              Input('soil-mineral', 'n_clicks'),
              Input('literacy-india','n_clicks'),
              Input('hatecrime-india', 'n_clicks'),
              State('upload-data', 'filename'),
              prevent_initial_call=True
)
def update_output(contents, soil, literacy, hate, filename):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if input_id == 'upload-data':
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        message = ""
        error_message = "File in not in CSV format"
        try:
            if '.csv' in filename:
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
                message = 'Done'
                val = create_table(df.iloc[:10, :6])
                store_data = get_data_initial(df)
        except Exception as e:
            message = 'Error'
            error_message = e
            
        if message == 'Done':
            return False, 'green', "Success!!, Table uploaded",f"Having Rows - {df.shape[0]} and Columns - {df.shape[1]}. Showing first 10 rows",no_update,no_update,no_update,no_update,'check', val, no_update, store_data
        else:
            return False, 'red', error_message," ", no_update,no_update,no_update,no_update,'check', no_update, no_update,no_update
    else:
        if input_id =='soil-mineral':
            df = pd.read_csv('assets/data/soil.csv')
            val = create_table(df.iloc[:10, :6])
            store_data = get_data_initial(df)
        elif input_id == 'literacy-india':
            df = pd.read_csv('assets/data/literacy.csv')
            val = create_table(df.iloc[:10, :6])
            store_data = get_data_initial(df)
        elif input_id == 'hatecrime-india':
            df = pd.read_csv('assets/data/hate_crime.csv')
            val = create_table(df.iloc[:10, :6])
            store_data = get_data_initial(df)
        return no_update,no_update,no_update,no_update,False,'green','Data Loaded', f"Having Rows - {df.shape[0]} and Columns - {df.shape[1]}. Showing first 10 rows", '',no_update,val,store_data



#CB3 -  populate all drowpdown
dash.clientside_callback(
    """
    function update_dropdown(clicks1, clicks2,active, data) {
        var ctx = dash_clientside.callback_context;
        var prop_id = ctx.triggered[0]['prop_id'];
        if ((prop_id === 'next-kmean.n_clicks' && active === 0) || (prop_id === 'back-kmean.n_clicks' && active === 2)) {
            var column_data = data.available_column.map(obj => obj.column)
            //console.log(column_data);
            var column_val = data.available_column_val.map(obj => obj.column_val)
            var row_data = data.available_row.map(obj => obj.row)
            var selection = data.model_selection.map(obj => obj.row)
            var trimmed_data = data.new_row.map(obj => obj.row)
            return [column_data, column_val, row_data, trimmed_data, row_data, trimmed_data, row_data,[row_data[0]],
                row_data, [row_data[0],row_data[1]],row_data, [row_data[0],row_data[1],row_data[2]], row_data, selection,row_data];
        } else{
            throw dash_clientside.PreventUpdate;
        }
    }
    """,
    Output('column-select', 'data'),
    Output('column-select', 'value'),
    Output('row-select', 'data'),
    Output('row-select', 'value'),
    Output('heatmap-columns', 'data'),
    Output('heatmap-columns', 'value'),
    Output('histogram-columns', 'data'),
    Output('histogram-columns', 'value'),
    Output('hist2d-columns', 'data'),
    Output('hist2d-columns', 'value'),
    Output('scatter-matrix-columns', 'data'),
    Output('scatter-matrix-columns', 'value'),
    Output('final-column-selection', 'data'),
    Output('final-column-selection', 'value'),
    Output('column-tolimit','data'),
    Input("back-kmean", "n_clicks"),
    Input("next-kmean", "n_clicks"),
    State("stepper-basic-usage", "active"),
    State('used-data', 'data'),
    prevent_initial_call=True
)
            
            
#CB4 - Checking null values
@dash.callback(
    Output('missing-value-table', 'children', allow_duplicate=True),
    Output('drop-null-btn-div','hidden', allow_duplicate=True),
    Input("back-kmean", "n_clicks"),
    Input("next-kmean", "n_clicks"),
    State("stepper-basic-usage", "active"),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def null_val(c1, c2, active,data):
    hidden=True
    ctx = dash.callback_context
    prop_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if (prop_id == 'next-kmean' and active==0) or (prop_id=='back-kmena' and active==2):
        get_data = pd.DataFrame(data['table'])
        ch1 = get_data.isna().sum().to_frame().reset_index()
        ch1.columns=['Variables', 'Missing Value Count']
        val = create_table(ch1)
        if get_data.isna().sum().sum() != 0:
            hidden=False
        return val, hidden
    else:
        raise PreventUpdate
        


#CB5 - droping null values 
@dash.callback(
    Output('missing-value-table', 'children'),
    Output('alert-missing-delete', 'children'),
    Output('alert-missing-delete', 'hide'),
    Output('used-data', 'data', allow_duplicate=True),
    Output('drop-null-btn-div','hidden'),
    Input('drop-missing-val', 'n_clicks'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def null_val_drop(n_clicks, data):
    get_data = pd.DataFrame(data['table'])
    init_row = get_data.shape[0]
    get_data.dropna(inplace=True, axis=0)
    ch1 = get_data.isna().sum().to_frame().reset_index()
    ch1.columns=['Variables', 'Missing Value Count']
    val = create_table(ch1)
    data['table'] = get_data.to_dict('records')
    
    numeric_cols = get_data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    n_df = get_data[numeric_cols]


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
    data['table_data'] = table_data
    diff = init_row - get_data.shape[0]
    return val, f'Done!!, droped {diff} rows', False, data,True



#CB6 - updating column descriptive statistic
dash.clientside_callback(
    """
    function( column_dropdown, row_dropdown, data) {
        const dropdown_data = row_dropdown;
        const columnsToDisplay = ['Variables'];
        column_dropdown.forEach((column)=>{
            columnsToDisplay.push(column);
        })
        
        //console.log('this is the one', dropdown_data, columnsToDisplay)
        
        const tableBody = document.getElementById('stats_data');
        //console.log('table', tableBody);
        tableBody.innerHTML = '';
        
        
        const tableData2 = data['table_data'];
        //console.log(tableData2)
        
        const tableData = tableData2.filter(({ Variables }) => dropdown_data.includes(Variables));
        //console.log(tableData)
        
        //adding heading hear
        
        let thead = document.createElement('thead');
        let headerRow = document.createElement('tr');
        columnsToDisplay.forEach((column) =>{
            var header = document.createElement('th');
            header.innerText = column;
            headerRow.appendChild(header)
        });
        thead.appendChild(headerRow);
        tableBody.appendChild(thead);
        
        //adding rows here

        var rows = tableData.forEach((item) => {
          const row = document.createElement('tr');
          
          //loop through column
          columnsToDisplay.forEach((column) => {
              var cell = document.createElement('td');
              
              cell.innerText = item[column];
              
              row.appendChild(cell);
          })
          tableBody.appendChild(row);
        })
        return rows;
        }
    """,
    Output('stats_data', 'children'),
    Input('column-select', 'value'),
    Input('row-select', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)

#CB7 - built heatmap
@dash.callback(
    Output('heatmap-fig', 'figure'),
    Input('heatmap-columns', 'value'),
    Input("back-kmean", "n_clicks"),
    Input("next-kmean", "n_clicks"),
    State("stepper-basic-usage", "active"),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def getheat(columns, nc, nc1,act, data):
    ctx = dash.callback_context
    prop_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if (prop_id == 'next-kmean' and active==0) or (prop_id=='back-kmena' and active==2) or (prop_id == 'heatmap-columns'):
        get_data = pd.DataFrame(data['table'])
        return getheatmap(get_data, col='not all', columns=columns)
    else:
        raise PreventUpdate


#CB8 - built histogram
@dash.callback(
    Output('histogram-fig', 'figure'),
    Input('histogram-columns', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def gethistogram_fn(columns, data):
    get_data = pd.DataFrame(data['table'])
    return gethistogram(get_data, columns=columns)


#CB9 - build 2d Hist
@dash.callback(
    Output('hist2d-fig', 'figure'),
    Output("hist2d-columns", "error"),
    Input('hist2d-columns', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def gethist2d(columns, data):
    if len(columns)<2:
        return dash.no_update, "Select at least 2."
    else:
        get_data = pd.DataFrame(data['table'])
        return gethist2d_fig(get_data, columns=columns, title=''), ""

#CB10 - build scatter matrix
@dash.callback(
    Output('scatter-matrix-fig', 'figure'),
    Output("scatter-matrix-columns", "error"),
    Input('scatter-matrix-columns', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def getscatter(columns, data):
    if len(columns)<3:
        return dash.no_update, "Select at least 3."
    else:
        get_data = pd.DataFrame(data['table'])
        return getscatter_fig(get_data, columns=columns, title=','.join(columns)), ""


#CB11 - outlier data
@dash.callback(
    Output('outlier-value-table', 'children', allow_duplicate=True),
    Input("back-kmean", "n_clicks"),
    Input("next-kmean", "n_clicks"),
    State("stepper-basic-usage", "active"),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def outlier_data(c1, c2, active,data):
    ctx = dash.callback_context
    prop_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if (prop_id == 'next-kmean' and active==0) or (prop_id=='back-kmena' and active==2):
        n_df = pd.DataFrame(data['table'])
        numeric_cols =n_df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        n_df=n_df[numeric_cols]
        dic = dict()
        for i in n_df.columns:
            lis = list()
            q1 = n_df[i].quantile(0.25)
            q3 = n_df[i].quantile(0.75)
            iqr = q3-q1
            thres1 = q3+1.5*iqr
            thres2 = q1-1.5*iqr
            try:
                lis.append((n_df[i]>thres1).value_counts()[True])
            except:
                lis.append(0)
            try:
                lis.append((n_df[i]<thres2).value_counts()[True])
            except:
                lis.append(0)
            dic[i] = lis
        ch1 = pd.DataFrame(dic).T.reset_index()
        ch1.columns=['Variables','Greater than upper threshold', 'Smaller the lower threshold']
        val = create_table(ch1)
        return val
    else:
        raise PreventUpdate

#CB12 - Update outlier data
@dash.callback(
    Output('outlier-value-table', 'children'),
    Output('alert-outlier-limit', 'hide'),
    Output('alert-outlier-limit2', 'hide'),
    Output('used-data', 'data', allow_duplicate=True),
    Input('limit-outlier-val', 'n_clicks'),
    State('used-data', 'data'),
    State('column-tolimit', 'value'),
    State('outlier-value-table', 'children'),
    prevent_initial_call=True
)
def update_outlier_data(c1, data,cols,child):

    if cols is not None:
        n_df = pd.DataFrame(data['table'])
        numeric_cols =n_df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        other_cols = [i for i in n_df.columns if i not in numeric_cols]
        o_df = n_df[other_cols]
        n_df=n_df[numeric_cols]
        dic = dict()
        for i in n_df.columns:
            
            lis = list()
            q1 = n_df[i].quantile(0.25)
            q3 = n_df[i].quantile(0.75)
            iqr = q3-q1
            thres1 = q3+1.5*iqr
            thres2 = q1-1.5*iqr
            if i in cols:
                n_df[i] = np.where(n_df[i]>thres1, thres1,n_df[i])
                n_df[i] = np.where(n_df[i]<thres2, thres2,n_df[i])
            try:
                lis.append((n_df[i]>thres1).value_counts()[True])
            except:
                lis.append(0)
            try:
                lis.append((n_df[i]<thres2).value_counts()[True])
            except:
                lis.append(0)
            dic[i] = lis
        ch1 = pd.DataFrame(dic).T.reset_index()
        ch1.columns=['Variables','Greater than upper threshold', 'Smaller the lower threshold']
        val = create_table(ch1)
        df = pd.concat([o_df, n_df], axis=1)
        data['table'] = df.to_dict('records')
        return val,False,True,data
    else:
        return child,True,False,data
  

#CB13 - update column selection
dash.clientside_callback(
    """
    function update_model_col(data) {
        var column_selected = data.model_selection.map(obj => obj.row)
        return "Selected Columns are :- " + column_selected.join(", ");
    }
    """,
    Output('final-select-show', 'children'),
    Input('used-data', 'data'),
    prevent_initial_call=True
)


#CB14 - store column 
@dash.callback(
    Output('used-data', 'data', allow_duplicate=True),
    Input('final-select', 'n_clicks'),
    State('final-column-selection', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def update_selection(click, value, data):
    data['model_selection'] = pd.DataFrame(value, columns=['row']).to_dict('records')
    return data


#CB15 - create elbow
@dash.callback(
    Output('elbow-graph', 'figure'),
    Input('standerdize-type', 'value'),
    Input('cluster-number-elbow', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def getelbow_data(value, n_cluster, data):
    return getelbow(data, value, n_cluster)


#CB16 - create model
@dash.callback(
    Output("model-done", "hide"),
    Output("model-error", "hide"),
    Output("used-data", 'data', allow_duplicate=True),
    Output("compute-model-overlay", 'children'),
    Input("compute-model", "n_clicks"),
    State("num-cluster", 'value'),
    State('used-data', 'data'),
    State('standerdize-type', 'value'),
    prevent_initial_call=True,
)
def alert_auto(n_clicks, value, data, stander):
    if value is None:
        return True, False, data, "Model Haven't Built yet!!!"
    else:
        value = [int(i) for i in value]
        data = create_model(data, value, stander)
        return False, True, data, "Model Building Completed"
    
#CB17 - populate dropdown cluster view page
dash.clientside_callback(
    """
    function update_dropdown2(clicks1, clicks2,active, data) {
        var ctx = dash_clientside.callback_context;
        var prop_id = ctx.triggered[0]['prop_id'];
        if ((prop_id === 'next-kmean.n_clicks' && active === 2) || (prop_id === 'back-kmean.n_clicks' && active === 4)){
            var cluster_data = data.cluster_list.map(obj => obj.cluster)
            var selection = data.model_selection.map(obj => obj.row)
            return [cluster_data, cluster_data[0], selection, selection, selection, selection[0],cluster_data, cluster_data[0],
            selection, [selection[0],selection[1],selection[2]],cluster_data, cluster_data[0],
            selection, [selection[0],selection[1],selection[2]],cluster_data, cluster_data[0],
            selection, selection,cluster_data, cluster_data[0]];
        } else{
            throw dash_clientside.PreventUpdate;
        }
    
    }
    
    """,
    Output('cluster-select', 'data'),
    Output('cluster-select', 'value'),
    Output('var-select', 'data'),
    Output('var-select', 'value'),
    Output('cluster-boxplot-columns', 'data'),
    Output('cluster-boxplot-columns', 'value'),
    Output('cluster-boxplot-select', 'data'),
    Output('cluster-boxplot-select', 'value'),
    Output('cluster-scatter-columns', 'data'),
    Output('cluster-scatter-columns', 'value'),
    Output('cluster-scatter-select', 'data'),
    Output('cluster-scatter-select', 'value'),
    Output('cluster-3dscatter-columns', 'data'),
    Output('cluster-3dscatter-columns', 'value'),
    Output('cluster-3dscatter-select', 'data'),
    Output('cluster-3dscatter-select', 'value'),
    Output('cluster-pca-columns', 'data'),
    Output('cluster-pca-columns', 'value'),
    Output('cluster-pca-select', 'data'),
    Output('cluster-pca-select', 'value'),
    Input("back-kmean", "n_clicks"),
    Input("next-kmean", "n_clicks"),
    State("stepper-basic-usage", "active"),
    State('used-data', 'data'),
    prevent_initial_call=True
)
            

#CB18 - Cluster stats
@dash.callback(
    Output('cluster_stats_data', 'children'),
    Input('cluster-select', 'value'),
    Input('var-select', 'value'),
    Input('stats-select', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def update_cluster_table(cluster, var, stat, data):
    df = pd.DataFrame(data['cluster_data'])[var+[cluster]]
    if stat == 'Mean':
        ch1 = round(df.groupby(cluster).agg('mean').T.reset_index(),2)
        ch1 = ch1.rename(columns={'index':'Variables'})
        val = create_table(ch1)
    elif stat == 'Median':
        ch1 = round(df.groupby(cluster).agg(np.median).T.reset_index(),2)
        ch1 = ch1.rename(columns={'index':'Variables'})
        val = create_table(ch1)
    elif stat == 'Mode':
        ch1 = round(df.groupby(cluster).agg(pd.Series.mode).T.reset_index(),2)
        ch1 = ch1.rename(columns={'index':'Variables'})
        val = create_table(ch1)
    elif stat == 'MAX':
        ch1 = round(df.groupby(cluster).agg('max').T.reset_index(),2)
        ch1 = ch1.rename(columns={'index':'Variables'})
        val = create_table(ch1)
    elif stat == 'MIN':
        ch1 = round(df.groupby(cluster).agg('min').T.reset_index(),2)
        ch1 = ch1.rename(columns={'index':'Variables'})
        val = create_table(ch1)
    return val


#CB19 - boxplot
@dash.callback(
    Output('cluster-boxplot-fig', 'figure'),
    Input('cluster-boxplot-columns', 'value'),
    Input('cluster-boxplot-select', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def getbox(column, cluster, data):

    df = pd.DataFrame(data['cluster_data'])[[column]+[cluster]]
    return getboxplot(df,cluster, column,title='')

#CB20 - scatter
@dash.callback(
    Output('cluster-scatter-fig', 'figure'),
    Output("cluster-scatter-columns", "error"),
    Input('cluster-scatter-columns', 'value'),
    Input('cluster-scatter-select', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def getscatter2(columns, cluster, data):
    if len(columns)<3:
        return dash.no_update, "Select at least 3."
    else:
        df = pd.DataFrame(data['cluster_data'])[columns+[cluster]]
        return getscatterplot(df, columns,cluster, title=''), ""

#CB21 - 3d Scatter
@dash.callback(
    Output('cluster-3dscatter-fig', 'figure'),
    Output("cluster-3dscatter-columns", "error"),
    Input('cluster-3dscatter-columns', 'value'),
    Input('cluster-3dscatter-select', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def get3dscatter(columns, cluster, data):
    if len(columns)<3:
        return dash.no_update, "Select at least 3."
    else:
        df = pd.DataFrame(data['cluster_data'])[columns+[cluster]]
        return get3dscatterplot(df, columns,cluster, title=''), ""

#CB22 - PCA2D
@dash.callback(
    Output('cluster-pca-fig', 'figure'),
    Output('cluster-pca-columns', 'error'),
    Input('pca2d-compute', 'n_clicks'),
    State('cluster-pca-columns', 'value'),
    State('cluster-pca-select', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def pca_2d(click, columns, cluster, data):
    if len(data['model_selection'])>4 and len(columns)<4:
        return dash.no_update, "Select at least 4."
    else:
        df = pd.DataFrame(data['cluster_data'])[columns+[cluster]]
        df[cluster] = df[cluster].apply(lambda x: f'c-{x}')
        pca = PCA(n_components=2)
        components = pca.fit_transform(df[columns])
        ch1 = pd.DataFrame(components)
        ch1.columns = ['var1', 'var2']
        ch1['cluster'] = df[cluster]
        fig = px.scatter(ch1, x='var1', y='var2', color='cluster', category_orders={'cluster':[f'c-{x}' for x in np.arange(int(cluster.split('_')[-1]))]})
        fig.update_layout(
            plot_bgcolor="#fff",
            font=dict(color='#999999'),
            height=500,
            margin=dict(t=0, l=0, r=0, b=0, pad=0,autoexpand=True),
            legend=dict(orientation='h', y=1.1),
          )
        return fig, ""

#CB23 - PCA3D
@dash.callback(
    Output('cluster-pca3d-fig', 'figure'),
    Input('pca3d-compute', 'n_clicks'),
    State('cluster-pca-columns', 'value'),
    State('cluster-pca-select', 'value'),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def pca_3d(click, columns, cluster, data):
    if len(data['model_selection'])>4 and len(columns)<4:
        return dash.no_update
    else:
        df = pd.DataFrame(data['cluster_data'])[columns+[cluster]]
        df[cluster] = df[cluster].apply(lambda x: f'c-{x}')
        pca = PCA(n_components=3)
        components = pca.fit_transform(df[columns])
        ch1 = pd.DataFrame(components)
        ch1.columns = ['var1', 'var2', 'var3']
        ch1['cluster'] = df[cluster]
        fig = px.scatter_3d(ch1, x='var1', y='var2', z='var3', color='cluster', category_orders={'cluster':[f'c-{x}' for x in np.arange(int(cluster.split('_')[-1]))]})
        fig.update_layout(
            plot_bgcolor="#fff",
            font=dict(color='#999999'),
            height=500,
            margin=dict(t=0, l=0, r=0, b=0, pad=0,autoexpand=True),
            legend=dict(orientation='h', y=1.1),
          )
        return fig

#CB24 - Download
@dash.callback(
    Output("download_xslx", "data"), 
    Input("btn_xslx", "n_clicks"),
    State('used-data', 'data'),
    prevent_initial_call=True
)
def generate_xlsx(n_nlicks, data):
        
    
    df = pd.DataFrame(data['cluster_data'])
    df2 = pd.DataFrame(data['table'])
    col=[i for i in df2.columns if i not in df.columns]
    df = pd.concat([df2[col], df], axis=1)
    def to_xlsx(bytes_io):
        xslx_writer = pd.ExcelWriter(bytes_io, engine="xlsxwriter")  # requires the xlsxwriter package
        df.to_excel(xslx_writer, sheet_name="sheet1")
        xslx_writer.save()

    return dcc.send_bytes(to_xlsx, "clusters.xlsx")
