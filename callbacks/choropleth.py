from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

def register_choropleth_callbacks(app, df, df_timelapse):
    """
    Registers callbacks for choropleth maps.

    Args:
        app: Dash application instance
        df: Main DataFrame
        df_timelapse: Timelapse DataFrame
    """
    @app.callback(
        Output('choropleth-container', 'children'),
        [Input('choropleth-dropdown', 'value')]
    )
    def update_choropleth(selected_value):
        if selected_value == 'growth-rate':
            fig = px.choropleth(
                df_timelapse,
                locations="ISO3",
                color="Growth Rate (%)",
                hover_name="Country_FR",
                animation_frame="Year",
                color_continuous_scale="RdYlGn",
                range_color=[-5, 9],
                title="Taux de croissance (%) de la population (1960–2018)",
                labels={
                    "Growth Rate (%)": "Taux de croissance (%)",
                    "Year": "Année"
                }
            )
            fig.update_layout(
                geo=dict(showframe=False, showcoastlines=False),
                height=600
            )
        
        elif selected_value == 'absolute-growth':
            fig = px.choropleth(
                df,
                locations="ISO3",
                color="Population Growth",
                hover_name="Country_FR",
                animation_frame="Year",
                color_continuous_scale="RdBu",
                range_color=[-1_000_000, 1_000_000],
                title="Croissance absolue de la population par pays (échelle fixe à 1M)",
                labels={
                    "Population Growth": "Croissance absolue",
                    "Year": "Année"
                }
            )
            fig.update_layout(
                geo=dict(showframe=False, showcoastlines=False),
                height=600
            )
        
        elif selected_value == 'population-fixed':
            vmin = df[df["Year"] == 1960]["Population"].min()
            vmax = 100_000_000
            fig = px.choropleth(
                df,
                locations="ISO3",
                color="Population",
                hover_name="Country_FR",
                animation_frame="Year",
                color_continuous_scale="YlGnBu",
                range_color=[vmin, vmax],
                title="Population par pays (échelle fixe à 100M)",
                labels={
                    "Population Growth": "Croissance absolue",
                    "Year": "Année"
                }
            )
            fig.update_layout(
                coloraxis_colorbar=dict(
                    title="Population",
                    tickformat=".0s"
                ),
                geo=dict(showframe=False, showcoastlines=False),
                height=600
            )
        
        return dcc.Graph(figure=fig)