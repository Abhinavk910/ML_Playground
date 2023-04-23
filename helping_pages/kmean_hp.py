# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 01:25:20 2023

@author: abhinav.kumar
"""

from dash import html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import numpy as np
from helping_functions.kmean_fx import blank_fig

innerContainerWidth = '1100px'
innerheadingsize=20




#Load Data
data_page1 = dmc.Container(
            style={'maxWidth':innerContainerWidth},
            children=[
                dcc.Store(id='store-data', data = None, storage_type='session'),
                dmc.Accordion(
                    id="accordion-simple",
                    value="choose",
                    variant='saperated',
                    children=[
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Upload", icon=DashIconify(icon='material-symbols:upload-file-outline')),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Text(
                                            children=[
                                                dcc.Upload(
                                                    id='upload-data',
                                                    multiple=False,
                                                    style={
                                                        'lineHeight': '30px','borderWidth': '1px','borderStyle': 'dashed',
                                                        'borderRadius': '3px','borderColor':'rgba(0,0,0,0.3)','textAlign': 'center','margin': '5px',
                                                        'padding':'20px', 'backgroundColor':'white'
                                                    },
                                                    children=[
                                                        dmc.Stack(
                                                            align='center',
                                                            spacing='1px',
                                                            children=[
                                                                DashIconify(icon="material-symbols:upload-rounded", width=50,color='rgba(0,0,0,0.4)'),
                                                                dmc.Text('Drag and Drop or Choose file to upload'),
                                                                dmc.Text('CSV only', color='rgba(0,0,0,0.4)', weight=700)

                                                            ]
                                                        )
                                                    ],
                                                ),
                                                dmc.LoadingOverlay(
                                                    dmc.Stack(
                                                        children=[
                                                            dmc.Text('FOr overlay', id='check1', style={'color':'whitesmoke', 'height':'40px'}),
                                                            dmc.Alert( title="Success!", color="green", id='alert-check',
                                                                      icon=DashIconify(icon="mdi:success-circle-outline"),
                                                                      duration=60000,hide=True, style={'marginTop':'-40px'}),
                                                            html.Div(
                                                                dmc.Table(
                                                                    striped=True,
                                                                    highlightOnHover=True,
                                                                    withBorder=True,
                                                                    withColumnBorders=True,
                                                                    id='table-data',
                                                                ),
                                                                style={'overflowX':'scroll'}
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ]
                                ),
                            ],
                            value="Upload",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Sample Dataset", icon=DashIconify(icon="material-symbols:dataset-outline")),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Stack(
                                            children=[
                                                dmc.Grid(
                                                    mb=30,
                                                    gutter='xl',
                                                    justify='space-around',
                                                    align='stretch',
                                                    children=[
                                                        dmc.Col(
                                                            span=12,
                                                            md=4,
                                                            children=[
                                                                dmc.Card(
                                                                    children=[
                                                                        dmc.CardSection(
                                                                            dmc.Image(
                                                                                src="assets/image/soil.jpg",
                                                                                height=160,
                                                                            )
                                                                        ),
                                                                        dmc.Text(
                                                                            mt=10,
                                                                            children=[
                                                                                'Soil Mineral Content Across Different Districts of India'
                                                                            ]
                                                                        ),
                                                                        dmc.Button('Get Data',mt=10,
                                                                                   leftIcon=DashIconify(icon="fluent:database-plug-connected-20-filled"),
                                                                                   id='soil-mineral', variant='gradient', size='xs')
                                                                    ]
                                                                ),
                                                            ]
                                                        ),
                                                        dmc.Col(
                                                            span=12,
                                                            md=4,
                                                            children=[
                                                                dmc.Card(
                                                                    children=[
                                                                        dmc.CardSection(
                                                                            dmc.Image(
                                                                                src="assets/image/literacy.jpg",
                                                                                height=160,
                                                                            )
                                                                        ),
                                                                        dmc.Text(
                                                                            mt=10,
                                                                            children=[
                                                                                'Literacy Rate Across Different Districts of India'
                                                                            ]
                                                                        ),
                                                                        dmc.Button('Get Data',mt=10,
                                                                                   leftIcon=DashIconify(icon="fluent:database-plug-connected-20-filled"),
                                                                                   id='literacy-india', variant='gradient', size='xs')
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        dmc.Col(
                                                            span=12,
                                                            md=4,
                                                            children=[
                                                                dmc.Card(
                                                                    children=[
                                                                        dmc.CardSection(
                                                                            dmc.Image(
                                                                                src="assets/image/hate.jpg",
                                                                                height=160,
                                                                            )
                                                                        ),
                                                                        dmc.Text(
                                                                            mt=10,
                                                                            children=[
                                                                                'Hate and Crime Across Different Districts of India'
                                                                            ]
                                                                        ),
                                                                        dmc.Button('Get Data',mt=10,
                                                                                   leftIcon=DashIconify(icon="fluent:database-plug-connected-20-filled"),
                                                                                   id='hatecrime-india', variant='gradient', size='xs')
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                dmc.Alert( title="Success!", color="green", id='alert-check2',
                                                      icon=DashIconify(icon="mdi:success-circle-outline"),
                                                      duration=60000,hide=True, style={'marginTop':'-40px'}
                                                ),
                                                html.Div(
                                                    dmc.Table(
                                                        striped=True,
                                                        highlightOnHover=True,
                                                        withBorder=True,
                                                        withColumnBorders=True,
                                                        id='table-data2',
                                                    ),
                                                    style={'overflowX':'scroll'}
                                                )
                                            ]
                                        )
                                    ]
                                ),
                            ],
                            value="choose",
                        ),
                    ],
                )
            ]
        )


#Data Cleaning
header = [
    html.Thead(
        html.Tr(
            [
                html.Th("Variables"),
                html.Th("Missing Value Count")
            ]
        )
    )
]
row1 = html.Tr([html.Td("var1"), html.Td("0")])
body = [html.Tbody([row1])]

data_page2 =dmc.Container(
            style={'maxWidth':innerContainerWidth},
            children=[
                html.Div(
                    id="hidden-div",
                    style={"display": "none"},
                    children="This callback is triggered when the page loads",
                ),
                dmc.Accordion(
                    id="feature-engg-accordion",
                    value="missing-value-check",
                    variant='saperated',
                    children=[
                        dmc.AccordionItem(
                            value="missing-value-check",
                            children = [
                                dmc.AccordionControl("Missing Value Check", icon=DashIconify(icon='grommet-icons:document-missing')),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Stack(
                                            align='center',
                                            justify='center',
                                            children=[
                                                dmc.Center(
                                                    dmc.LoadingOverlay(
                                                        html.Div(
                                                            dmc.Table(
                                                                id='missing-value-table', 
                                                                children=header+body,
                                                                striped=True,
                                                                highlightOnHover=True,
                                                                withBorder=True,
                                                                withColumnBorders=True
                                                            ),
                                                            style={'overflowX':'scroll', 'minWidth':'300px'}
                                                        )
                                                    )
                                                ),
                                                html.Div(
                                                    dmc.Button('Drop Missing Row', id='drop-missing-val',
                                                               leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                               variant='gradient'),
                                                    hidden=True,
                                                    id='drop-null-btn-div'
                                                ),
                                                dmc.Alert(id='alert-missing-delete', color='green',hide=True,
                                                          icon=DashIconify(icon='clarity:success-standard-solid'),
                                                          duration=3000)
                                            ]
                                        )
                                    ]
                                ),
                            ],  
                        ),
                        dmc.AccordionItem(
                            value="discriptive_stats",
                            children=[
                                dmc.AccordionControl("Column Profiling", icon=DashIconify(icon="gridicons:stats")),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Stack(
                                            children=[
                                                dmc.Text('Basic Stats', weight=700, mt=5, size=innerheadingsize),
                                                dmc.Grid(
                                                    align='stretch',
                                                    justify='space-around',
                                                    grow=1,
                                                    style={'width':'100%'},
                                                    gutter='xs',
                                                    children=[
                                                        dmc.Col(
                                                            span=6,
                                                            sm=4,
                                                            md=3,
                                                            order=1,
                                                            children=[
                                                                dmc.MultiSelect(
                                                                    id='column-select',
                                                                    searchable=True,
                                                                    nothingFound="No options found",
                                                                    clearable=True,
                                                                    icon=DashIconify(icon='ion:stats-chart-outline'),
                                                                    description='Stats',
                                                                )
                                                            ]
                                                        ),
                                                        dmc.Col(
                                                            span=6,
                                                            sm=4,
                                                            md=3,
                                                            order=0,
                                                            children=[
                                                                dmc.MultiSelect(
                                                                    id='row-select',
                                                                    style={'heigth':'100vh'},
                                                                    searchable=True,
                                                                    nothingFound="No options found",
                                                                    clearable=True,
                                                                    icon=DashIconify(icon='mdi:variable'),
                                                                    description='Variables',

                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    dmc.Table(
                                                        id='stats_data',
                                                        striped=True,
                                                        highlightOnHover=True,
                                                        withBorder=True,
                                                        withColumnBorders=True,
                                                    ),
                                                    style={'overflowX':'scroll', 'minWidth':'300px'}
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('Correlation Matrix', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.MultiSelect(
                                                            id='heatmap-columns',
                                                            description='Variables',
                                                            searchable=True,
                                                            nothingFound="No options found",
                                                            icon=DashIconify(icon='mdi:variable'),
                                                            clearable=True,
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='heatmap-fig',
                                                            )
                                                        )
                                                        
                                                    ]
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('Distribution', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.MultiSelect(
                                                            id='histogram-columns',
                                                            description='Variables',
                                                            searchable=True,
                                                            nothingFound="No options found",
                                                            clearable=True,
                                                            icon=DashIconify(icon='mdi:variable'),
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='histogram-fig',
                                                            )
                                                        )
                                                        
                                                    ]
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('Density Plot', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.MultiSelect(
                                                            id='hist2d-columns',
                                                            maxSelectedValues=2,
                                                            description='Variables',
                                                            searchable=True,
                                                            nothingFound="No options found",
                                                            icon=DashIconify(icon='mdi:variable'),
                                                            clearable=True,
                                                            
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='hist2d-fig',
                                                            )
                                                        )
                                                        
                                                    ]
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('Scatter Matrix', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.MultiSelect(
                                                            id='scatter-matrix-columns',
                                                            description='Variables',
                                                            icon=DashIconify(icon='mdi:variable'),
                                                            searchable=True,
                                                            nothingFound="No options found",
                                                            clearable=True,
                                                            
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='scatter-matrix-fig',
                                                            )
                                                        )
                                                        
                                                    ]
                                                ),
                                            ]
                                        )
                                    ]
                                ),
                            ],   
                        ),
                        dmc.AccordionItem(
                            value="outlier-value-check",
                            
                            children = [
                                dmc.AccordionControl("Outlier Check", icon=DashIconify(icon='ph:arrow-square-out')),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Stack(
                                            children=[
                                                dmc.Text('Threshold calculation is Based on IQR'),
                                                dmc.LoadingOverlay(
                                                    html.Div(
                                                        dmc.Table(id='outlier-value-table',                                                                striped=True,
                                                                    highlightOnHover=True,
                                                                    withBorder=True,
                                                                    withColumnBorders=True,
                                                        ),
                                                        style={'overflowX':'scroll', 'minWidth':'300px'}
                                                    ),
                                                ),
                                                dmc.MultiSelect(
                                                    label="Variables",
                                                    description='Removing Outlier by thresholding values',
                                                    id='column-tolimit',
                                                    icon=DashIconify(icon='mdi:variable'),
                                                    searchable=True,
                                                    nothingFound="No options found",
                                                    clearable=True,
                                                    
                                                ),
                                                dmc.Button('Limit the Outlier', id='limit-outlier-val',
                                                           leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                           variant='gradient'),
                                                dmc.Alert(children=['Done'],id='alert-outlier-limit', color='green',
                                                          icon=DashIconify(icon='clarity:success-standard-solid'),hide=True,
                                                          duration=3000),
                                                dmc.Alert(children=['Select atleast one!!!'],id='alert-outlier-limit2', color='yellow',
                                                          icon=DashIconify(icon='material-symbols:info-outline-rounded'),hide=True,
                                                          duration=3000)
                                            ]
                                        )
                                    ]
                                ),
                            ],  
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Column Selection", icon=DashIconify(icon='material-symbols:view-column-outline-rounded')),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Stack(
                                            children=[
                                                dmc.MultiSelect(
                                                    label="Available Variable",
                                                    id='final-column-selection',
                                                    description='Selected Variable which will be used in building Model',
                                                    searchable=True,
                                                    icon=DashIconify(icon='mdi:variable'),
                                                    nothingFound="No options found",
                                                    clearable=True,
                                                ),
                                                dmc.Button(['Select'], id='final-select',
                                                           leftIcon=DashIconify(icon="iconoir:open-select-hand-gesture"),
                                                           variant='gradient',size='md'),
                                                dmc.LoadingOverlay(
                                                dmc.Text(id='final-select-show'))
                                            ]
                                        )
                                    ]
                                ),
                            ],
                            value="column_selection",
                        ),
                    ],
                )   
            ]
        )


#Model Building
data_page3=dmc.Container(
            style={'maxWidth':innerContainerWidth},
            children=[
                dmc.Accordion(
                    id="model-accordion",
                    value="Standerdize",
                    variant='saperated',
                    children=[
                        dmc.AccordionItem(
                            value="Standerdize",
                            children=[
                                dmc.AccordionControl("Data Transformation", icon=DashIconify(icon="carbon:chart-median")),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Spoiler(
                                            showLabel="Show more",
                                            hideLabel="Hide",
                                            maxHeight=36,
                                            children=[
                                                dmc.Text(
                                                    size=13,
                                                    color='dimmed',
                                                    children=[
                                                    """Data transformation is important in K-means clustering because the algorithm is based on Euclidean distance, which is sensitive to differences in scale and variance between variables. If your data includes variables that are on vastly different scales or have different variances, the K-means algorithm may be biased towards variables with larger scales or variances. This can lead to clusters that are based more on these variables than on the others, and can distort the overall clustering solution.

                                                       By transforming the data, you can ensure that all variables have a similar scale and variance, which can help to remove this bias and ensure that each variable contributes equally to the clustering solution. There are several common data transformations that can be used for this purpose, such as scaling, standardization, and normalization.

                                                       For example, Normalization involves converting each variable to a common scale, such as between 0 and 1 or -1 and 1, by dividing each value by the maximum value of that variable. Standardization involves transforming the data so that each variable has a mean of 0 and a standard deviation of 1.

                                                       By performing data transformation, you can improve the accuracy and reliability of your K-means clustering results, and ensure that each variable is given equal weight in the final clustering solution. """
                                                    ]
                                                )
                                            ],
                                        ),
                                        dmc.Select(
                                            style={'marginTop':'20px'},
                                            description='Scalling Type',
                                            data=["Standardization", "Normalization"],
                                            searchable=True,
                                            nothingFound="No options found",
                                            id='standerdize-type',
                                            icon = DashIconify(icon="uil:scaling-right")
                                        )
                                    ]
                                )
                            ]
                        ),
                        dmc.AccordionItem(
                            value="elbow",
                            children=[
                                dmc.AccordionControl("Elbow", icon=DashIconify(icon="game-icons:elbow-pad")),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Spoiler(
                                            showLabel="Show more",
                                            hideLabel="Hide",
                                            maxHeight=36,
                                            children=[
                                                dmc.Text(
                                                    size=13,
                                                    color='dimmed',
                                                    children=[
                                                        """The elbow method is a technique used to determine the optimal number of clusters to use in a K-means clustering algorithm. The method involves plotting the within-cluster sum of squared errors (WCSS) for a range of cluster values and identifying the "elbow" in the plot, which represents the point of diminishing returns where the increase in the number of clusters no longer results in a significant reduction in WCSS.
                                                    """
                                                    ]
                                                )
                                            ],
                                        ),
                                        dmc.NumberInput(
                                            label="Select Cluster",
                                            description='WCSS will be calculated on these cluster',
                                            value=10,
                                            min=1,
                                            step=1,
                                            icon=DashIconify(icon='carbon:assembly-cluster'),
                                            style={'marginBottom':'20px'},
                                            id='cluster-number-elbow'
                                        ),
                                        dmc.LoadingOverlay(
                                            dcc.Graph(id='elbow-graph', figure=blank_fig())
                                        )
                                    ]
                                )
                            ]
                        ),
                        dmc.AccordionItem(
                            value="model",
                            children=[
                                dmc.AccordionControl("Model", icon=DashIconify(icon="carbon:model-alt")),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.MultiSelect(
                                            style={'marginBottom':'20px'},
                                            label='Create Model with Cluster',
                                            description='Can Select more than one',
                                            icon=DashIconify(icon='carbon:assembly-cluster'),
                                            data=[str(i) for i in np.arange(1, 20).tolist()],
                                            id='num-cluster'
                                        ),
                                        dmc.Button('Compute', id='compute-model',
                                                   leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                   variant='gradient', style={'margin':'10px', 'width':'100%'}),
                                        dmc.LoadingOverlay(dmc.Text(children=["Model Haven't Built yet"],style={'margin':'10px'},id='compute-model-overlay', size=23)),
                                        dmc.Alert(
                                            "Model Building Process completed. Click Next for Cluster Analysis",
                                            title="Done",
                                            id="model-done",
                                            color="success",
                                            duration=3000,
                                            hide=True
                                        ),
                                        dmc.Alert(
                                            "You have to select atleast one cluster",
                                            title="Error",
                                            id="model-error",
                                            color="red",
                                            duration=3000,
                                            hide=True
                                        ),
                                    ]
                                )
                            ]
                        )    
                    ]
                )
            ]
        )


#cluster Viewing
data_page4= dmc.Container(
            style={'maxWidth':innerContainerWidth},
            children=[
                dmc.Accordion(
                    id="cluster-accordion",
                    value="clusterP2",
                    variant='saperated',
                    children=[

                        dmc.AccordionItem(
                            value="clusterP2",
                            children=[
                                dmc.AccordionControl("Cluster Profiling", icon=DashIconify(icon="gridicons:stats")),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Stack(
                                            children=[
                                                dmc.Text('Basic Stats of Different Clusters', weight=700, mt=5, size=innerheadingsize),
                                                dmc.Grid(
                                                    align='stretch',
                                                    justify='space-around',
                                                    grow=1,
                                                    style={'width':'100%', 'marginTop':'5px', 'marginBottom':'5px'},
                                                    gutter='xs',
                                                    children=[
                                                        dmc.Col(
                                                            span=4,
                                                            sm=4,
                                                            md=3,
                                                            order=0,
                                                            children=[
                                                                dmc.Select(
                                                                    id='cluster-select',
                                                                    icon=DashIconify(icon='carbon:assembly-cluster'),
                                                                    description='Cluster',
                                                                )
                                                            ]
                                                        ),
                                                        dmc.Col(
                                                            span=4,
                                                            sm=4,
                                                            md=3,
                                                            order=1,
                                                            children=[
                                                                dmc.MultiSelect(
                                                                    id='var-select',
                                                                    icon=DashIconify(icon='mdi:variable'),
                                                                    description='Variables',
                                                                    searchable=True,
                                                                    nothingFound="No options found",
                                                                    clearable=True,
                                                                )
                                                            ]
                                                        ),
                                                        dmc.Col(
                                                            span=4,
                                                            sm=4,
                                                            md=3,
                                                            order=2,
                                                            children=[
                                                                dmc.Select(
                                                                    id='stats-select',
                                                                    data=['Mean', 'Median', 'Mode', 'MIN', 'MAX'],
                                                                    icon=DashIconify(icon='ion:stats-chart-outline'),
                                                                    description='Stats',
                                                                    value='Mean'

                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                dmc.LoadingOverlay(
                                                    html.Div(
                                                        dmc.Table(
                                                            striped=True,
                                                            highlightOnHover=True,
                                                            withBorder=True,
                                                            withColumnBorders=True,
                                                            id='cluster_stats_data'
                                                        ),
                                                        style={'overflowX':'scroll', 'minWidth':'300px'}
                                                    )
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('Distribution Of Cluster', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.Grid(
                                                            align='stretch',
                                                            justify='space-around',
                                                            grow=1,
                                                            style={'width':'100%', 'marginTop':'5px', 'marginBottom':'5px'},
                                                            gutter='xs',
                                                            children=[
                                                                dmc.Col(
                                                                    span=6,
                                                                    sm=4,
                                                                    md=3,
                                                                    order=1,
                                                                    children=[
                                                                        dmc.Select(
                                                                            id='cluster-boxplot-select',
                                                                            icon=DashIconify(icon='carbon:assembly-cluster'),
                                                                            description='Cluster',
                                                                        ),
                                                                    ]
                                                                ),
                                                                dmc.Col(
                                                                    span=6,
                                                                    sm=4,
                                                                    md=3,
                                                                    order=0,
                                                                    children=[
                                                                        dmc.Select(
                                                                            id='cluster-boxplot-columns',
                                                                            icon=DashIconify(icon='mdi:variable'),
                                                                            description='Variable',
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='cluster-boxplot-fig',figure=blank_fig()
                                                            )
                                                        )

                                                    ]
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('Scatter Plot -  Cluster', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.Grid(
                                                            align='stretch',
                                                            justify='space-around',
                                                            grow=1,
                                                            style={'width':'100%', 'marginTop':'5px', 'marginBottom':'5px'},
                                                            gutter='xs',
                                                            children=[
                                                                dmc.Col(
                                                                    span=6,
                                                                    sm=4,
                                                                    md=3,
                                                                    order=1,
                                                                    children=[
                                                                        dmc.Select(
                                                                            id='cluster-scatter-select',
                                                                            icon=DashIconify(icon='carbon:assembly-cluster'),
                                                                            description='Cluster',
                                                                        ),
                                                                    ]
                                                                ),
                                                                dmc.Col(
                                                                    span=6,
                                                                    sm=4,
                                                                    md=3,
                                                                    order=0,
                                                                    children=[
                                                                        dmc.MultiSelect(
                                                                            id='cluster-scatter-columns',
                                                                            icon=DashIconify(icon='mdi:variable'),
                                                                            description='Variable',
                                                                            searchable=True,
                                                                            nothingFound="No options found",
                                                                            clearable=True,
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='cluster-scatter-fig', figure=blank_fig()
                                                            )
                                                        )

                                                    ]
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('3D Scatter Plot -  Cluster', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.Grid(
                                                            align='center',
                                                            justify='space-around',
                                                            grow=1,
                                                            style={'width':'100%', 'marginTop':'5px', 'marginBottom':'5px'},
                                                            gutter='xs',
                                                            children=[
                                                                dmc.Col(
                                                                    span=6,
                                                                    sm=4,
                                                                    md=3,
                                                                    order=1,
                                                                    children=[
                                                                        dmc.Select(
                                                                            id='cluster-3dscatter-select',
                                                                            icon=DashIconify(icon='carbon:assembly-cluster'),
                                                                            description='Cluster',
                                                                        ),
                                                                    ]
                                                                ),
                                                                dmc.Col(
                                                                    span=6,
                                                                    sm=4,
                                                                    md=3,
                                                                    order=0,
                                                                    children=[
                                                                        dmc.MultiSelect(
                                                                            id='cluster-3dscatter-columns',
                                                                            icon=DashIconify(icon='mdi:variable'),
                                                                            description='Variable',
                                                                            maxSelectedValues=3
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='cluster-3dscatter-fig', figure=blank_fig()
                                                            )
                                                        )

                                                    ]
                                                ),
                                            ]
                                        )
                                    ]
                                ),
                            ],   
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Cluster Distribution", icon=DashIconify(icon='uil:horizontal-distribution-center')),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Text('PCA Decomposing 2D', weight=700, mt=5, size=innerheadingsize),
                                        dmc.Text('PCA can be a useful technique for visualizing clusters in high-dimensional data. By reducing the number of dimensions, it becomes easier to plot the data and visualize the clusters in two or three dimensions.', color='dimmed', size=13),
                                        dmc.Stack(
                                            children=[
                                                dmc.Grid(
                                                    align='stretch',
                                                    justify='space-around',
                                                    grow=1,
                                                    style={'width':'100%','marginTop':'5px', 'marginBottom':'5px'},
                                                    gutter='xs',
                                                    children=[
                                                        dmc.Col(
                                                            span=6,
                                                            sm=4,
                                                            md=3,
                                                            order=1,
                                                            children=[
                                                                dmc.Select(
                                                                    id='cluster-pca-select',
                                                                    icon=DashIconify(icon='carbon:assembly-cluster'),
                                                                    description='Cluster',
                                                                ),
                                                            ]
                                                        ),
                                                        dmc.Col(
                                                            span=6,
                                                            sm=4,
                                                            md=3,
                                                            order=0,
                                                            children=[
                                                                dmc.MultiSelect(
                                                                    id='cluster-pca-columns',
                                                                    icon=DashIconify(icon='mdi:variable'),
                                                                    description='Variable',
                                                                    searchable=True,
                                                                    nothingFound='Nothing Found',
                                                                    clearable=True
                                                                ),
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                dmc.Button('Compute', id='pca2d-compute',
                                                           leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                           variant='gradient', style={'marginBottom':'5px'}),
                                                dmc.LoadingOverlay(
                                                    dcc.Graph(
                                                        id='cluster-pca-fig',figure=blank_fig()
                                                    )
                                                )
                                            ]
                                        ),
                                        dmc.Divider(),
                                        dmc.Stack(
                                            children=[
                                                dmc.Text('PCA Decomposing 3D', weight=700, mt=5, size=innerheadingsize),
                                                dmc.Button('Compute 3D', id='pca3d-compute',
                                                           leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                           variant='gradient', style={'marginBottom':'5px'}),
                                                dmc.LoadingOverlay(
                                                    dcc.Graph(
                                                        id='cluster-pca3d-fig', figure=blank_fig()
                                                    )
                                                )
                                            ]
                                        )
                                    ]
                                ),
                            ],
                            value="pca",
                        )
                    ],
                )   
            ]
        )