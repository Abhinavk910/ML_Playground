# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:49:53 2023

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
                dmc.Accordion(
                    id="accordion-simple-ml3",
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
                                                    id='upload-data-ml3',
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
                                                            dmc.Text('FOr overlay', id='check1-ml3', style={'color':'whitesmoke', 'height':'40px'}),
                                                            dmc.Alert( title="Success!", color="green", id='alert-check-ml3',
                                                                      icon=DashIconify(icon="mdi:success-circle-outline"),
                                                                      duration=60000,hide=True, style={'marginTop':'-40px'}),
                                                            html.Div(
                                                                dmc.Table(
                                                                    striped=True,
                                                                    highlightOnHover=True,
                                                                    withBorder=True,
                                                                    withColumnBorders=True,
                                                                    id='table-data-ml3',
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
                                                                                   id='soil-mineral-ml3', variant='gradient', size='xs')
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
                                                                                   id='literacy-india-ml3', variant='gradient', size='xs')
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
                                                                                   id='hatecrime-india-ml3', variant='gradient', size='xs')
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                dmc.Alert( title="Success!", color="green", id='alert-check2-ml3',
                                                      icon=DashIconify(icon="mdi:success-circle-outline"),
                                                      duration=60000,hide=True, style={'marginTop':'-40px'}
                                                ),
                                                html.Div(
                                                    dmc.Table(
                                                        striped=True,
                                                        highlightOnHover=True,
                                                        withBorder=True,
                                                        withColumnBorders=True,
                                                        id='table-data2-ml3',
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
                    id="hidden-div-ml3",
                    style={"display": "none"},
                    children="This callback is triggered when the page loads",
                ),
                dmc.Accordion(
                    id="feature-engg-accordion-ml3",
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
                                                                id='missing-value-table-ml3', 
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
                                                    dmc.Button('Drop Missing Row', id='drop-missing-val-ml3',
                                                               leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                               variant='gradient'),
                                                    hidden=True,
                                                    id='drop-null-btn-div-ml3'
                                                ),
                                                dmc.Alert(id='alert-missing-delete-ml3', color='green',hide=True,
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
                                                                    id='column-select-ml3',
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
                                                                    id='row-select-ml3',
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
                                                        id='stats_data-ml3',
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
                                                            id='heatmap-columns-ml3',
                                                            description='Variables',
                                                            searchable=True,
                                                            nothingFound="No options found",
                                                            icon=DashIconify(icon='mdi:variable'),
                                                            clearable=True,
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='heatmap-fig-ml3',
                                                            )
                                                        )
                                                        
                                                    ]
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('Distribution', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.MultiSelect(
                                                            id='histogram-columns-ml3',
                                                            description='Variables',
                                                            searchable=True,
                                                            nothingFound="No options found",
                                                            clearable=True,
                                                            icon=DashIconify(icon='mdi:variable'),
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='histogram-fig-ml3',
                                                            )
                                                        )
                                                        
                                                    ]
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('Density Plot', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.MultiSelect(
                                                            id='hist2d-columns-ml3',
                                                            maxSelectedValues=2,
                                                            description='Variables',
                                                            searchable=True,
                                                            nothingFound="No options found",
                                                            icon=DashIconify(icon='mdi:variable'),
                                                            clearable=True,
                                                            
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='hist2d-fig-ml3',
                                                            )
                                                        )
                                                        
                                                    ]
                                                ),
                                                dmc.Divider(),
                                                dmc.Stack(
                                                    children=[
                                                        dmc.Text('Scatter Matrix', weight=700, mt=5, size=innerheadingsize),
                                                        dmc.MultiSelect(
                                                            id='scatter-matrix-columns-ml3',
                                                            description='Variables',
                                                            icon=DashIconify(icon='mdi:variable'),
                                                            searchable=True,
                                                            nothingFound="No options found",
                                                            clearable=True,
                                                            
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='scatter-matrix-fig-ml3',
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
                                                        dmc.Table(id='outlier-value-table-ml3',                                                                striped=True,
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
                                                    id='column-tolimit-ml3',
                                                    icon=DashIconify(icon='mdi:variable'),
                                                    searchable=True,
                                                    nothingFound="No options found",
                                                    clearable=True,
                                                    
                                                ),
                                                dmc.Button('Limit the Outlier', id='limit-outlier-val-ml3',
                                                           leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                           variant='gradient'),
                                                dmc.Alert(children=['Done'],id='alert-outlier-limit-ml3', color='green',
                                                          icon=DashIconify(icon='clarity:success-standard-solid'),hide=True,
                                                          duration=3000),
                                                dmc.Alert(children=['Select atleast one!!!'],id='alert-outlier-limit2-ml3', color='yellow',
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
                                                    id='final-column-selection-ml3',
                                                    description='Selected Variable which will be used in building Model',
                                                    searchable=True,
                                                    icon=DashIconify(icon='mdi:variable'),
                                                    nothingFound="No options found",
                                                    clearable=True,
                                                ),
                                                dmc.Button(['Select'], id='final-select-ml3',
                                                           leftIcon=DashIconify(icon="iconoir:open-select-hand-gesture"),
                                                           variant='gradient',size='md'),
                                                dmc.LoadingOverlay(
                                                dmc.Text(id='final-select-show-ml3'))
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
                    id="model-accordion-ml3",
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
                                            id='standerdize-type-ml3',
                                            icon = DashIconify(icon="uil:scaling-right")
                                        )
                                    ]
                                )
                            ]
                        ),
                        dmc.AccordionItem(
                            value="dendrogram",
                            children=[
                                dmc.AccordionControl("Dendrogram", icon=DashIconify(icon="mdi:family-tree")),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.LoadingOverlay(
                                            dcc.Graph(id='dendrogram-graph', figure=blank_fig(),config={'displayModeBar': False})
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
                                            data=[str(i) for i in np.arange(2, 20).tolist()],
                                            id='num-cluster-ml3'
                                        ),
                                        dmc.Button('Compute', id='compute-model-ml3',
                                                   leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                   variant='gradient', style={'margin':'10px', 'width':'100%'}),
                                        dmc.LoadingOverlay(dmc.Text(children=["Model Haven't Built yet"],style={'margin':'10px'},id='compute-model-overlay-ml3', size=23)),
                                        dmc.Alert(
                                            "Model Building Process completed. Click Next for Cluster Analysis",
                                            title="Done",
                                            id="model-done-ml3",
                                            color="success",
                                            duration=3000,
                                            hide=True
                                        ),
                                        dmc.Alert(
                                            "You have to select atleast one cluster",
                                            title="Error",
                                            id="model-error-ml3",
                                            color="red",
                                            duration=3000,
                                            hide=True
                                        ),
                                        dmc.Table(
                                            id='cluster-table-ml3',
                                            striped=True,
                                            highlightOnHover=True,
                                            withBorder=True,
                                            withColumnBorders=True
                                        ),
                                    ]
                                )
                            ]
                        ),
                        dmc.AccordionItem(
                            value='surrogate_model',
                            children=[
                                dmc.AccordionControl("Feature Importance", icon=DashIconify(icon="material-symbols:label-important-outline")),
                                dmc.AccordionPanel(
                                    style={'padding':'10px 20px 10px 20px',}, 
                                    children=[
                                        dmc.Text(
                                            size=13,
                                            color='dimmed',
                                            children=[
                                            """Using a decision tree as a surrogate model to calculate feature importance is a common technique in machine learning.""",
                                            """The basic idea is to train a decision tree on the same data that was used to generate the clustering results, but with the cluster assignments as the target variable.""",
                                            """The decision tree can then be used to estimate the importance of each input feature in determining the cluster assignments. """
                                            ]
                                        ),
                                        dmc.Select(
                                            style={'marginTop':'20px'},
                                            description='Select Cluster',
                                            searchable=True,
                                            nothingFound="No options found",
                                            id='feature-importance-clusters-ml3',
                                            icon = DashIconify(icon="uil:scaling-right")
                                        ),
                                        dmc.Button('Compute importance', id='compute-model-importance-ml3',
                                                   leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                   variant='gradient', style={'margin':'10px', 'width':'100%'}),
                                        dmc.LoadingOverlay(
                                            dcc.Graph(
                                                id='feature-importance-fig-ml3', figure=blank_fig(), config={'displayModeBar': False}
                                            )
                                        )
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
                    id="cluster-accordion-ml3",
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
                                                                    id='cluster-select-ml3',
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
                                                                    id='var-select-ml3',
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
                                                                    id='stats-select-ml3',
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
                                                            id='cluster_stats_data-ml3'
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
                                                                            id='cluster-boxplot-select-ml3',
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
                                                                            id='cluster-boxplot-columns-ml3',
                                                                            icon=DashIconify(icon='mdi:variable'),
                                                                            description='Variable',
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        dmc.LoadingOverlay(
                                                            dcc.Graph(
                                                                id='cluster-boxplot-fig-ml3',figure=blank_fig()
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
                                                                            id='cluster-scatter-select-ml3',
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
                                                                            id='cluster-scatter-columns-ml3',
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
                                                                id='cluster-scatter-fig-ml3', figure=blank_fig()
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
                                                                            id='cluster-3dscatter-select-ml3',
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
                                                                            id='cluster-3dscatter-columns-ml3',
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
                                                                id='cluster-3dscatter-fig-ml3', figure=blank_fig()
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
                                                                    id='cluster-pca-select-ml3',
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
                                                                    id='cluster-pca-columns-ml3',
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
                                                dmc.Button('Compute', id='pca2d-compute-ml3',
                                                           leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                           variant='gradient', style={'marginBottom':'5px'}),
                                                dmc.LoadingOverlay(
                                                    dcc.Graph(
                                                        id='cluster-pca-fig-ml3',figure=blank_fig()
                                                    )
                                                )
                                            ]
                                        ),
                                        dmc.Divider(),
                                        dmc.Stack(
                                            children=[
                                                dmc.Text('PCA Decomposing 3D', weight=700, mt=5, size=innerheadingsize),
                                                dmc.Button('Compute 3D', id='pca3d-compute-ml3',
                                                           leftIcon=DashIconify(icon="clarity:process-on-vm-line"),
                                                           variant='gradient', style={'marginBottom':'5px'}),
                                                dmc.LoadingOverlay(
                                                    dcc.Graph(
                                                        id='cluster-pca3d-fig-ml3', figure=blank_fig()
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