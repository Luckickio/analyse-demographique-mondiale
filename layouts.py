from dash import dcc, html

def create_layout():
    """
    Creates the layout of the Dash application.

    Returns:
        html.Div: Complete layout of the application
    """
    return html.Div([
        html.H1("Analyse Démographique Mondiale (1960-2018)", style={'textAlign': 'center'}),
        
        dcc.Tabs([
            dcc.Tab(label='Cartes Choroplèthes', children=[
                html.Div([
                    html.H3("Sélectionner la visualisation:", style={'marginTop': '20px'}),
                    dcc.Dropdown(
                        id='choropleth-dropdown',
                        options=[
                            {'label': 'Taux de croissance de la population', 'value': 'growth-rate'},
                            {'label': 'Croissance absolue de la population (échelle fixe à 1M)', 'value': 'absolute-growth'},
                            {'label': 'Population par pays (échelle fixe à 100M)', 'value': 'population-fixed'}
                        ],
                        value='growth-rate'
                    ),
                    html.Div(id='choropleth-container', style={'marginTop': '20px'})
                ])
            ]),
            
            dcc.Tab(label='Comparaisons par pays', children=[
                html.Div([
                    html.H3("Sélectionner la visualisation:", style={'marginTop': '20px'}),
                    dcc.Dropdown(
                        id='countries-dropdown',
                        options=[
                            {'label': 'Top 10 pays les plus peuplés', 'value': 'top10'},
                            {'label': 'Pays du G7', 'value': 'g7'},
                            {'label': 'Pays émergents', 'value': 'emerging'},
                            {'label': 'Russie post-URSS', 'value': 'russia'},
                            {'label': 'Rwanda (impact du génocide)', 'value': 'rwanda'},
                            {'label': 'Pays en déclin ou stagnation démographique', 'value': 'decline'}
                        ],
                        value='top10'
                    ),
                    html.Div(id='countries-container', style={'marginTop': '20px'})
                ])
            ]),
            
            dcc.Tab(label='Analyse continentale', children=[
                html.Div([
                    html.H3("Sélectionner la visualisation:", style={'marginTop': '20px'}),
                    dcc.Dropdown(
                        id='continents-dropdown',
                        options=[
                            {'label': 'Évolution de la population par continent', 'value': 'continent-evolution'},
                            {'label': 'Nombre de pays par continent', 'value': 'continent-countries'}
                        ],
                        value='continent-evolution'
                    ),
                    html.Div(id='continents-container', style={'marginTop': '20px'})
                ])
            ]),
            
            dcc.Tab(label='Tendances mondiales', children=[
                html.Div([
                    html.H3("Sélectionner la visualisation:", style={'marginTop': '20px'}),
                    dcc.Dropdown(
                        id='global-dropdown',
                        options=[
                            {'label': 'Croissance moyenne de la population par année', 'value': 'avg-growth'},
                            {'label': 'Évolution de la population mondiale totale', 'value': 'total-population'}
                        ],
                        value='avg-growth'
                    ),
                    html.Div(id='global-container', style={'marginTop': '20px'})
                ])
            ])
        ])
    ])