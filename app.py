# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 23:28:04 2023

@author: abhinav.kumar
"""

from dash import Dash, html, Output, Input, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import dash
from dash_iconify import DashIconify

def get_icon(icon):
    return DashIconify(icon=icon, height=16, color="#c2c7d0")


app = Dash(__name__, 
           use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[
               {"name": "viewport", "content": "width=device-width, initial-scale=1"}
             ],
            suppress_callback_exceptions=True
           )

server = app.server


app.layout = dmc.MantineProvider(
        theme={
            'fontFamily': '"Inter", sans-serif',
            },
        children=[
            dmc.Container([
                dmc.Navbar(
                    py="md",
                    pl='xs',
                    pr=0,
                    fixed=False,
                    width={"base": 300},
                    hidden=True,
                    hiddenBreakpoint='md',
                    position='right',
                    height='100vh',
                    id='sidebar2',
                    sx={'&:hover':{'width': '300px'}},
                    children=[
                        html.Div(
                            [
                                dmc.NavLink(
                                    label="Clustering",
                                    icon=get_icon(icon="carbon:assembly-cluster"),
                                    childrenOffset=35,
                                    opened=True,
                                    children=[
                                        dmc.NavLink(label="KMean",
                                                    href='/kmean',
                                                    icon=get_icon(icon='carbon:edge-cluster')),
                                    ],
                                ),
                                                    ],
                            style={'whiteSpace': 'nowrap'},
                        )],style={'overflow':'hidden', 'transition': 'width 0.3s ease-in-out', 'backgroundColor':''}
                    ),      
                dmc.Drawer(
                        #title="Company Name",
                        id="drawer-simple2",
                        padding="md",
                        zIndex=10000,
                        size=300,
                        overlayOpacity=0.1,
                        children=[
                            html.Div(
                                [
                                    dmc.NavLink(
                                        label="Clustering",
                                        icon=get_icon(icon="carbon:assembly-cluster"),
                                        childrenOffset=35,
                                        opened=True,
                                        children=[
                                            dmc.NavLink(label="KMean",
                                                        href='/kmean',
                                                        icon=get_icon(icon='carbon:edge-cluster')),
                                        ],
                                    ),
                                ],
                                style={'whiteSpace': 'nowrap'},
                            )
                        ], style={'backgroundColor':''}, styles={'drawer':{'backgroundColor':''}}),
                dmc.Container(
                    id="page-container2",
                    p=0,
                    fluid=True,
                    style={'backgroundColor':'#f4f6f9', 'width':'100%', 'margin':'0'},
                    children=[
                        dmc.Header(
                            height=50,
                            p='10px',
                            style={"backgroundColor": ""},
                            children=[
                                dmc.Group(
                                    position='apart',
                                    children=[
                                        html.Div(
                                            children=[
                                                dmc.MediaQuery([
                                                    dmc.ActionIcon(
                                                        DashIconify(icon="solar:hamburger-menu-outline", color="grey"),
                                                        variant="subtle", 
                                                        p=0,
                                                        id='sidebar-button2'
                                                    ),
                                                    ], smallerThan="md", styles={'display': 'none'}),
                                                dmc.MediaQuery([
                                                    dmc.ActionIcon(
                                                        DashIconify(icon="solar:hamburger-menu-outline",color="grey"),
                                                        variant="subtle", 
                                                        p=0,
                                                        id='drawer-demo-button2'
                                                    ),
                                                    ], largerThan="md", styles={'display': 'none'}),
                                            ]
                                        ),
                                        html.Div(
                                            dmc.Group(
                                                children=[
                                                      dmc.Text(['Created By ',
                                                                dmc.Anchor("Abhinav Kumar",href="http://www.linkedin.com/in/abhinavk910",
                                                                        target="_blank", style={'text-decoration': 'none', 'color':'#457b9d'})
                                                      ], align='center', color="#a8dadc", weight=700),  
                                                    html.A(
                                                        dmc.Avatar(src='assets/head.jpg',
                                                            size="xs",radius="lg"),
                                                    href="https://abhinavk910.github.io/portfolio/",
                                                    target="_blank",
                                                    ),
                                                    html.A(
                                                        dmc.Avatar(DashIconify(icon="mdi:linkedin", width=15, color="#a8dadc"),#'#0a66c2'
                                                            size="xs",radius="xs"),
                                                    href="http://www.linkedin.com/in/abhinavk910",
                                                    target="_blank",
                                                    ),
                                                    html.A(
                                                        dmc.Avatar(DashIconify(icon="mdi:github", width=15, color="#a8dadc"),#'#24292f'
                                                            size="xs",radius="xs"),
                                                    href="https://github.com/Abhinavk910/Data-Visualization/tree/main/apps/Makeover_Mondays",
                                                    target="_blank",
                                                    )
                                                ], spacing='xs', position='right'
                                            )
                                        )
                                    ]
                                )
                            ]
                        ),
                        dash.page_container
                    ],
                )
            ], size='100%', p=0,m=0, style={'display':'flex'}
        )
    ]
)




        
dash.clientside_callback(
    """    
    function handle_click(n_clicks){
      if (n_clicks > 0) {
        return true;
      } else {
        return '';
      }
    }
    """,
    Output("drawer-simple2", "opened"),
    Input("drawer-demo-button2", "n_clicks")
)



dash.clientside_callback(
    """
    function handle_click_sidebar_width(n_clicks, width){
      const current_width = parseInt(width.base)
      if (n_clicks > 0 & current_width == 300) {
       return {base: 55};
      } else {
        return {base:300};
      }
    }
    """,
    Output("sidebar2", "width"),
    Input("sidebar-button2", "n_clicks"),
    State('sidebar2','width')
)

if __name__ == '__main__':
	app.run_server(debug=True, port=8051)