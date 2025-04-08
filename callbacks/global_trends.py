from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

def register_global_callbacks(app, df):
    """
    Registers callbacks for global trends.

    Args:
        app: Dash application instance
        df: Main DataFrame
    """
    @app.callback(
        Output('global-container', 'children'),
        [Input('global-dropdown', 'value')]
    )
    def update_global(selected_value):
        if selected_value == 'avg-growth':
            df_year_growth_avg = df.groupby('Year')['Population Growth'].mean().reset_index()
            
            fig = px.scatter(
                df_year_growth_avg,
                x="Year",
                y="Population Growth",
                title="Croissance de la population moyenne par année",
                labels={"Population Growth": "Croissance de la Population", "Year": "Année"}
            )
            
            fig.update_layout(
                plot_bgcolor="white",
                xaxis=dict(showgrid=True, gridcolor="lightgray"),
                yaxis=dict(showgrid=True, gridcolor="lightgray"),
                height=600
            )
        
        elif selected_value == 'total-population':
            df_year_population_total = df.groupby('Year')['Population'].sum().reset_index()
            
            fig = px.scatter(
                df_year_population_total,
                x="Year",
                y="Population",
                title="Évolution de la population totale mondiale par année",
                labels={"Population": "Population Totale", "Year": "Année"}
            )
            
            fig.update_layout(
                plot_bgcolor="white",
                xaxis=dict(showgrid=True, gridcolor="lightgray"),
                yaxis=dict(showgrid=True, gridcolor="lightgray"),
                height=600
            )
        
        return dcc.Graph(figure=fig)