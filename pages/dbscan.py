# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:20:29 2023

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
from helping_pages.dbscan_hp import data_page1, data_page2, data_page3, data_page4
from helping_functions.kmean_fx import get_data_initial, create_table, getheatmap,gethistogram,gethist2d_fig, getscatter_fig, getboxplot, getscatterplot, get3dscatterplot
from helping_functions.dbscan_fx import get_db_cluster, getfeature_importance

dash.register_page(__name__)

min_step = 0
max_step = 4
active2 = 0

layout = html.Div([
        dmc.Container(
            style={'backgroundColor':'whitesmoke','marginTop':'0.2rem','padding':'1rem',
                   'minHeight':'100vh', 'maxWidth':'1200px'},
            children=[
                dcc.Store(id='used-data-ml2', data=None, storage_type='session'),
                dmc.Stepper(
                    id="stepper-basic-usage-ml2",
                    active=active2,
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
                            id='step2-ml2',
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
                                        dmc.Button("Download xlsx", id="btn_xslx-ml2",
                                               leftIcon=DashIconify(icon="material-symbols:download-rounded"),
                                               style={'width':'200px', 'margin':'auto'}),
                                        dcc.Download(id="download_xslx-ml2")
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
                            dmc.Button("Back", id="back-kmean-ml2", variant="default",leftIcon=DashIconify(icon="material-symbols:arrow-back")),
                            id='back-div-ml2',
                            hidden=False
                        ),
                        html.Div(
                            dmc.Button("Next step", id="next-kmean-ml2",variant='gradient', rightIcon=DashIconify(icon="material-symbols:arrow-forward")),
                            id='next-div-ml2',
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
            if (prop_id === 'back-kmean-ml2.n_clicks') {
                if(state > 0){
                return state - 1;
                } else {
                    return state
                }
            } else if (prop_id === 'next-kmean-ml2.n_clicks') {
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
    Output("stepper-basic-usage-ml2", "active"),
    Input("back-kmean-ml2", "n_clicks"),
    Input("next-kmean-ml2", "n_clicks"),
    State("stepper-basic-usage-ml2", "active"),
    prevent_initial_call=True
)
                
# CB2 - stepper button hide                  
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
    Output("next-div-ml2", "hidden"),
    Output('back-div-ml2', 'hidden'),
    Input("stepper-basic-usage-ml2", "active")
)
                 
                    

#CB3 -  uploading table and storing
@dash.callback(Output('alert-check-ml2', 'hide'),Output('alert-check-ml2', 'color'),Output('alert-check-ml2', 'title'),Output('alert-check-ml2', 'children'),
              Output('alert-check2-ml2', 'hide'),Output('alert-check2-ml2', 'color'),Output('alert-check2-ml2', 'title'),Output('alert-check2-ml2', 'children'),
              Output('check1-ml2', 'value'),Output('table-data-ml2', 'children'),Output('table-data2-ml2', 'children'),
              Output('used-data-ml2', 'data', allow_duplicate=True),
              Input('upload-data-ml2', 'contents'),
              Input('soil-mineral-ml2', 'n_clicks'),
              Input('literacy-india-ml2','n_clicks'),
              Input('hatecrime-india-ml2', 'n_clicks'),
              State('upload-data-ml2', 'filename'),
              prevent_initial_call=True
)
def update_output2(contents, soil, literacy, hate, filename):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if input_id == 'upload-data-ml2':
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
    elif input_id =='soil-mineral-ml2':
            df = pd.read_csv('assets/data/soil.csv')
            val = create_table(df.iloc[:10, :6])
            store_data = get_data_initial(df)
            return no_update,no_update,no_update,no_update,False,'green','Data Loaded', f"Having Rows - {df.shape[0]} and Columns - {df.shape[1]}. Showing first 10 rows", '',no_update,val,store_data
    elif input_id == 'literacy-india-ml2':
            df = pd.read_csv('assets/data/literacy.csv')
            val = create_table(df.iloc[:10, :6])
            store_data = get_data_initial(df)
            return no_update,no_update,no_update,no_update,False,'green','Data Loaded', f"Having Rows - {df.shape[0]} and Columns - {df.shape[1]}. Showing first 10 rows", '',no_update,val,store_data
    elif input_id == 'hatecrime-india-ml2':
            df = pd.read_csv('assets/data/hate_crime.csv')
            val = create_table(df.iloc[:10, :6])
            store_data = get_data_initial(df)
            return no_update,no_update,no_update,no_update,False,'green','Data Loaded', f"Having Rows - {df.shape[0]} and Columns - {df.shape[1]}. Showing first 10 rows", '',no_update,val,store_data
    else:
        raise PreventUpdate


#CB4 -  populate all drowpdown
dash.clientside_callback(
    """
    function update_dropdown(clicks1, clicks2,active, data) {
        var ctx = dash_clientside.callback_context;
        var prop_id = ctx.triggered[0]['prop_id'];
        if ((prop_id === 'next-kmean-ml2.n_clicks' && active === 0) || (prop_id === 'back-kmean-ml2.n_clicks' && active === 2)) {
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
    Output('column-select-ml2', 'data'),
    Output('column-select-ml2', 'value'),
    Output('row-select-ml2', 'data'),
    Output('row-select-ml2', 'value'),
    Output('heatmap-columns-ml2', 'data'),
    Output('heatmap-columns-ml2', 'value'),
    Output('histogram-columns-ml2', 'data'),
    Output('histogram-columns-ml2', 'value'),
    Output('hist2d-columns-ml2', 'data'),
    Output('hist2d-columns-ml2', 'value'),
    Output('scatter-matrix-columns-ml2', 'data'),
    Output('scatter-matrix-columns-ml2', 'value'),
    Output('final-column-selection-ml2', 'data'),
    Output('final-column-selection-ml2', 'value'),
    Output('column-tolimit-ml2','data'),
    Input("back-kmean-ml2", "n_clicks"),
    Input("next-kmean-ml2", "n_clicks"),
    State("stepper-basic-usage-ml2", "active"),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
            
            
#CB5 - Checking null values
@dash.callback(
    Output('missing-value-table-ml2', 'children', allow_duplicate=True),
    Output('drop-null-btn-div-ml2','hidden', allow_duplicate=True),
    Input("back-kmean-ml2", "n_clicks"),
    Input("next-kmean-ml2", "n_clicks"),
    State("stepper-basic-usage-ml2", "active"),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
def null_val(c1, c2, active,data):
    hidden=True
    ctx = dash.callback_context
    prop_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if (prop_id == 'next-kmean-ml2' and active==0) or (prop_id=='back-kmean-ml2' and active==2):
        get_data = pd.DataFrame(data['table'])
        ch1 = get_data.isna().sum().to_frame().reset_index()
        ch1.columns=['Variables', 'Missing Value Count']
        val = create_table(ch1)
        if get_data.isna().sum().sum() != 0:
            hidden=False
        return val, hidden
    else:
        raise PreventUpdate
        


#CB6 - droping null values 
@dash.callback(
    Output('missing-value-table-ml2', 'children'),
    Output('alert-missing-delete-ml2', 'children'),
    Output('alert-missing-delete-ml2', 'hide'),
    Output('used-data-ml2', 'data', allow_duplicate=True),
    Output('drop-null-btn-div-ml2','hidden'),
    Input('drop-missing-val-ml2', 'n_clicks'),
    State('used-data-ml2', 'data'),
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



#CB7 - updating column descriptive statistic
dash.clientside_callback(
    """
    function( column_dropdown, row_dropdown, data) {
        const dropdown_data = row_dropdown;
        const columnsToDisplay = ['Variables'];
        column_dropdown.forEach((column)=>{
            columnsToDisplay.push(column);
        })
        
        //console.log('this is the one', dropdown_data, columnsToDisplay)
        
        const tableBody = document.getElementById('stats_data-ml2');
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
    Output('stats_data-ml2', 'children'),
    Input('column-select-ml2', 'value'),
    Input('row-select-ml2', 'value'),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)

#CB8 - built heatmap
@dash.callback(
    Output('heatmap-fig-ml2', 'figure'),
    Input('heatmap-columns-ml2', 'value'),
    Input("back-kmean-ml2", "n_clicks"),
    Input("next-kmean-ml2", "n_clicks"),
    State("stepper-basic-usage-ml2", "active"),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
def getheat(columns, nc, nc1,active, data):
    get_data = pd.DataFrame(data['table'])
    return getheatmap(get_data, col='not all', columns=columns)


#CB9 - built histogram
@dash.callback(
    Output('histogram-fig-ml2', 'figure'),
    Input('histogram-columns-ml2', 'value'),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
def gethistogram_fn(columns, data):
    get_data = pd.DataFrame(data['table'])
    return gethistogram(get_data, columns=columns)


#CB10 - build 2d Hist
@dash.callback(
    Output('hist2d-fig-ml2', 'figure'),
    Output("hist2d-columns-ml2", "error"),
    Input('hist2d-columns-ml2', 'value'),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
def gethist2d(columns, data):
    if len(columns)<2:
        return dash.no_update, "Select at least 2."
    else:
        get_data = pd.DataFrame(data['table'])
        return gethist2d_fig(get_data, columns=columns, title=''), ""

#CB11 - build scatter matrix
@dash.callback(
    Output('scatter-matrix-fig-ml2', 'figure'),
    Output("scatter-matrix-columns-ml2", "error"),
    Input('scatter-matrix-columns-ml2', 'value'),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
def getscatter(columns, data):
    if len(columns)<3:
        return dash.no_update, "Select at least 3."
    else:
        get_data = pd.DataFrame(data['table'])
        return getscatter_fig(get_data, columns=columns, title=','.join(columns)), ""


#CB12 - outlier data
@dash.callback(
    Output('outlier-value-table-ml2', 'children', allow_duplicate=True),
    Input("back-kmean-ml2", "n_clicks"),
    Input("next-kmean-ml2", "n_clicks"),
    State("stepper-basic-usage-ml2", "active"),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
def outlier_data(c1, c2, active,data):

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

#CB13 - Update outlier data
@dash.callback(
    Output('outlier-value-table-ml2', 'children'),
    Output('alert-outlier-limit-ml2', 'hide'),
    Output('alert-outlier-limit2-ml2', 'hide'),
    Output('used-data-ml2', 'data', allow_duplicate=True),
    Input('limit-outlier-val-ml2', 'n_clicks'),
    State('used-data-ml2', 'data'),
    State('column-tolimit-ml2', 'value'),
    State('outlier-value-table-ml2', 'children'),
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
  

#CB14 - update column selection
dash.clientside_callback(
    """
    function update_model_col(data) {
        var column_selected = data.model_selection.map(obj => obj.row)
        return "Selected Columns are :- " + column_selected.join(", ");
    }
    """,
    Output('final-select-show-ml2', 'children'),
    Input('used-data-ml2', 'data'),
    prevent_initial_call=True
)


#CB15 - store column 
@dash.callback(
    Output('used-data-ml2', 'data', allow_duplicate=True),
    Input('final-select-ml2', 'n_clicks'),
    State('final-column-selection-ml2', 'value'),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
def update_selection(click, value, data):
    data['model_selection'] = pd.DataFrame(value, columns=['row']).to_dict('records')
    return data



#CB16 - create model
@dash.callback(
    Output("model-done-ml2", "hide"),
    Output("model-error-ml2", "hide"),
    Output("used-data-ml2", 'data', allow_duplicate=True),
    Output("compute-model-overlay-ml2", 'children'),
    Output("cluster-table-ml2", 'children'),
    Input("compute-model-ml2", "n_clicks"),
    State("eps-ml2", 'value'),
    State("min-samples-ml2", 'value'),
    State('used-data-ml2', 'data'),
    State('standerdize-type-ml2', 'value'),
    prevent_initial_call=True,
)
def create_model_ml2(click, eps, min_s, data, stand):
    try:
        data, val = get_db_cluster(data, eps, min_s, stand)
        return False, True, data, "Model Building Completed", val
    except Exception as e:
        return True, False, data, f"Model Building Error - {e}", None
    
#CB17 - populate dropdown cluster view page
dash.clientside_callback(
    """
    function update_dropdown2(clicks1, clicks2,active, data) {
        var ctx = dash_clientside.callback_context;
        var prop_id = ctx.triggered[0]['prop_id'];
        if ((prop_id === 'next-kmean-ml2.n_clicks' && active === 2) || (prop_id === 'back-kmean-ml2.n_clicks' && active === 4)){
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
    Output('cluster-select-ml2', 'data'),
    Output('cluster-select-ml2', 'value'),
    Output('var-select-ml2', 'data'),
    Output('var-select-ml2', 'value'),
    Output('cluster-boxplot-columns-ml2', 'data'),
    Output('cluster-boxplot-columns-ml2', 'value'),
    Output('cluster-boxplot-select-ml2', 'data'),
    Output('cluster-boxplot-select-ml2', 'value'),
    Output('cluster-scatter-columns-ml2', 'data'),
    Output('cluster-scatter-columns-ml2', 'value'),
    Output('cluster-scatter-select-ml2', 'data'),
    Output('cluster-scatter-select-ml2', 'value'),
    Output('cluster-3dscatter-columns-ml2', 'data'),
    Output('cluster-3dscatter-columns-ml2', 'value'),
    Output('cluster-3dscatter-select-ml2', 'data'),
    Output('cluster-3dscatter-select-ml2', 'value'),
    Output('cluster-pca-columns-ml2', 'data'),
    Output('cluster-pca-columns-ml2', 'value'),
    Output('cluster-pca-select-ml2', 'data'),
    Output('cluster-pca-select-ml2', 'value'),
    Input("back-kmean-ml2", "n_clicks"),
    Input("next-kmean-ml2", "n_clicks"),
    State("stepper-basic-usage-ml2", "active"),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
            

#CB18 - Cluster stats
@dash.callback(
    Output('cluster_stats_data-ml2', 'children'),
    Input('cluster-select-ml2', 'value'),
    Input('var-select-ml2', 'value'),
    Input('stats-select-ml2', 'value'),
    State('used-data-ml2', 'data'),
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
    Output('cluster-boxplot-fig-ml2', 'figure'),
    Input('cluster-boxplot-columns-ml2', 'value'),
    Input('cluster-boxplot-select-ml2', 'value'),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
def getbox(column, cluster, data):

    df = pd.DataFrame(data['cluster_data'])[[column]+[cluster]]
    return getboxplot(df,cluster, column,title='')

#CB20 - scatter
@dash.callback(
    Output('cluster-scatter-fig-ml2', 'figure'),
    Output("cluster-scatter-columns-ml2", "error"),
    Input('cluster-scatter-columns-ml2', 'value'),
    Input('cluster-scatter-select-ml2', 'value'),
    State('used-data-ml2', 'data'),
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
    Output('cluster-3dscatter-fig-ml2', 'figure'),
    Output("cluster-3dscatter-columns-ml2", "error"),
    Input('cluster-3dscatter-columns-ml2', 'value'),
    Input('cluster-3dscatter-select-ml2', 'value'),
    State('used-data-ml2', 'data'),
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
    Output('cluster-pca-fig-ml2', 'figure'),
    Output('cluster-pca-columns-ml2', 'error'),
    Input('pca2d-compute-ml2', 'n_clicks'),
    State('cluster-pca-columns-ml2', 'value'),
    State('cluster-pca-select-ml2', 'value'),
    State('used-data-ml2', 'data'),
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
    Output('cluster-pca3d-fig-ml2', 'figure'),
    Input('pca3d-compute-ml2', 'n_clicks'),
    State('cluster-pca-columns-ml2', 'value'),
    State('cluster-pca-select-ml2', 'value'),
    State('used-data-ml2', 'data'),
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


#CB24 - surrogate
@dash.callback(
    Output("feature-importance-fig-ml2", "figure"), 
    Input("compute-model-importance-ml2", "n_clicks"),
    State('used-data-ml2', 'data'),
    prevent_initial_call=True
)
def generate_surrogacy(n_nlicks, data):
    fig = getfeature_importance(data)
    return fig
    
    
        
    


#CB25 - Download
@dash.callback(
    Output("download_xslx-ml2", "data"), 
    Input("btn_xslx-ml2", "n_clicks"),
    State('used-data-ml2', 'data'),
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
